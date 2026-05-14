"""
customer_lookup.py
------------------
AWS Lambda function triggered by Amazon Connect.
When a customer calls, this function looks up their details
and passes the info back to the contact flow.

Beginner Concept: Lambda runs code WITHOUT needing a server.
Amazon Connect calls this function automatically during a call.
"""

import json
import boto3

# --- SAMPLE CUSTOMER DATABASE (In real projects, this would be DynamoDB or RDS) ---
MOCK_CUSTOMERS = {
    "9876543210": {"name": "Riya Sharma",   "account": "ACC001", "status": "active"},
    "9123456780": {"name": "Arjun Mehta",   "account": "ACC002", "status": "active"},
    "9000011111": {"name": "Priya Nair",    "account": "ACC003", "status": "suspended"},
}


def lambda_handler(event, context):
    """
    This is the MAIN function Lambda runs.
    'event'   = data sent by Amazon Connect (includes the caller's phone number)
    'context' = info about the Lambda environment (we don't use this here)
    """

    print("Received event from Amazon Connect:", json.dumps(event))

    # Step 1: Get the caller's phone number from the event
    # Amazon Connect sends it under 'CustomerEndpoint' -> 'Address'
    try:
        phone_number = event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
        # Remove the country code prefix if present (e.g., +91 -> last 10 digits)
        phone_number = phone_number.replace("+91", "").strip()
    except KeyError:
        # If the phone number isn't found, return a safe default
        return build_response("Unknown", "N/A", "unknown")

    # Step 2: Look up the customer in our database
    customer = MOCK_CUSTOMERS.get(phone_number)

    if customer:
        print(f"Customer found: {customer['name']}")
        return build_response(
            name=customer["name"],
            account=customer["account"],
            status=customer["status"]
        )
    else:
        print(f"No customer found for number: {phone_number}")
        return build_response("New Customer", "N/A", "new")


def build_response(name, account, status):
    """
    Helper function to build the response.
    Amazon Connect reads these key-value pairs and uses them in the contact flow.
    For example: "Hello, NAME! Your account status is STATUS."
    """
    return {
        "Name":          name,
        "AccountNumber": account,
        "AccountStatus": status
    }
