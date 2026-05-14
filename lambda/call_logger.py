"""
call_logger.py
--------------
AWS Lambda function that saves call details to Amazon S3.
This runs AFTER a call ends (triggered by Amazon Connect Contact Trace Records).

Beginner Concept: Amazon S3 is cloud storage — like Google Drive but for code/apps.
We store call logs here so we can analyse them later.
"""

import json
import boto3
import datetime

# The name of your S3 bucket — change this to your actual bucket name
S3_BUCKET_NAME = "my-connect-call-logs"

# Create an S3 client using boto3 (the AWS Python SDK)
s3_client = boto3.client("s3")


def lambda_handler(event, context):
    """
    Main handler: receives call data, formats it, and saves it to S3.
    """

    print("Call ended. Saving log to S3...")
    print("Event data:", json.dumps(event))

    # Step 1: Extract the important details from the event
    call_log = extract_call_details(event)

    # Step 2: Create a unique filename using the date and contact ID
    timestamp  = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    contact_id = call_log.get("ContactId", "unknown")
    file_name  = f"call-logs/{timestamp}_{contact_id}.json"

    # Step 3: Upload the log to S3
    try:
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(call_log, indent=2),
            ContentType="application/json"
        )
        print(f"✅ Log saved to s3://{S3_BUCKET_NAME}/{file_name}")
        return {"status": "success", "file": file_name}

    except Exception as e:
        print(f"❌ Failed to save log: {str(e)}")
        return {"status": "error", "message": str(e)}


def extract_call_details(event):
    """
    Pull the key fields we care about from the Amazon Connect event.
    Returns a clean dictionary we'll store as JSON.
    """
    return {
        "ContactId":       event.get("ContactId", "N/A"),
        "AgentId":         event.get("AgentId", "N/A"),
        "Queue":           event.get("Queue", {}).get("Name", "N/A"),
        "InitiationMethod": event.get("InitiationMethod", "N/A"),   # INBOUND, OUTBOUND, etc.
        "StartTimestamp":  event.get("InitiationTimestamp", "N/A"),
        "EndTimestamp":    event.get("DisconnectTimestamp", "N/A"),
        "Duration_seconds": event.get("AgentInteractionDuration", 0),
        "CustomerNumber":  event.get("CustomerEndpoint", {}).get("Address", "N/A"),
    }
