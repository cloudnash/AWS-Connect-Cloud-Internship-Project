"""
setup_connect.py
----------------
This script uses boto3 (AWS Python SDK) to automate the setup
of an Amazon Connect instance with basic configuration.

Beginner Concept: Instead of clicking through the AWS Console every time,
we write code to do it automatically. This is called "Infrastructure as Code."

Run this ONCE to set up your Connect instance programmatically.
"""

import boto3
import json

# --- CONFIGURATION — Edit these values before running ---
AWS_REGION      = "ap-south-1"          # e.g. Mumbai region
INSTANCE_ALIAS  = "my-contact-centre"   # Must be globally unique

# Create the Amazon Connect client
connect_client = boto3.client("connect", region_name=AWS_REGION)


def create_connect_instance():
    """
    Step 1: Create an Amazon Connect instance.
    This is the foundation — everything else lives inside it.
    """
    print("🔧 Creating Amazon Connect instance...")

    try:
        response = connect_client.create_instance(
            IdentityManagementType="CONNECT_MANAGED",  # Connect manages users internally
            InboundCallsEnabled=True,
            OutboundCallsEnabled=True,
            InstanceAlias=INSTANCE_ALIAS
        )
        instance_id = response["Id"]
        print(f"✅ Instance created! ID: {instance_id}")
        return instance_id

    except connect_client.exceptions.DuplicateResourceException:
        print(f"⚠️  Instance '{INSTANCE_ALIAS}' already exists. Skipping creation.")
        return get_existing_instance_id()

    except Exception as e:
        print(f"❌ Error creating instance: {e}")
        raise


def get_existing_instance_id():
    """Fetch the ID of an existing Connect instance by alias."""
    response = connect_client.list_instances()
    for instance in response.get("InstanceSummaryList", []):
        if instance.get("InstanceAlias") == INSTANCE_ALIAS:
            return instance["Id"]
    raise ValueError(f"No instance found with alias: {INSTANCE_ALIAS}")


def create_queue(instance_id, queue_name, description):
    """
    Step 2: Create a Queue inside the Connect instance.
    Queues hold customers while they wait for an agent.
    """
    print(f"📋 Creating queue: {queue_name}...")

    # First, get the default "Basic Queue" hours of operation ID
    hours_response = connect_client.list_hours_of_operations(InstanceId=instance_id)
    hours_id = hours_response["HoursOfOperationSummaryList"][0]["Id"]

    try:
        response = connect_client.create_queue(
            InstanceId=instance_id,
            Name=queue_name,
            Description=description,
            HoursOfOperationId=hours_id
        )
        queue_id = response["QueueId"]
        print(f"✅ Queue '{queue_name}' created! ID: {queue_id}")
        return queue_id

    except Exception as e:
        print(f"❌ Error creating queue '{queue_name}': {e}")
        return None


def main():
    """
    Main function — runs all setup steps in order.
    """
    print("=" * 50)
    print("  Amazon Connect Setup Script")
    print("=" * 50)

    # Step 1: Create Connect instance
    instance_id = create_connect_instance()

    # Step 2: Create queues for different departments
    queues_to_create = [
        ("General Support",  "Main queue for general customer inquiries"),
        ("Billing Support",  "Queue for billing and payment issues"),
        ("Technical Support","Queue for technical issues and escalations"),
    ]

    created_queues = {}
    for queue_name, description in queues_to_create:
        queue_id = create_queue(instance_id, queue_name, description)
        if queue_id:
            created_queues[queue_name] = queue_id

    # Step 3: Save the config to a file for reference
    config = {
        "instance_id": instance_id,
        "region": AWS_REGION,
        "queues": created_queues
    }
    with open("connect_config.json", "w") as f:
        json.dump(config, f, indent=2)

    print("\n✅ Setup complete! Config saved to connect_config.json")
    print(f"   Instance ID : {instance_id}")
    print(f"   Queues      : {list(created_queues.keys())}")
    print("\nNext step: Go to AWS Console → Amazon Connect to configure contact flows.")


if __name__ == "__main__":
    main()
