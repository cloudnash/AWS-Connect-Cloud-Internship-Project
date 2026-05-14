# 📦 Lambda Functions

These are the serverless functions that Amazon Connect calls during a customer interaction.

## Functions

| File | Trigger | What it does |
|---|---|---|
| `customer_lookup.py` | During call (Invoke Lambda block) | Finds customer info by phone number |
| `call_logger.py` | After call ends (CTR stream) | Saves call details to S3 |

## How to Deploy a Lambda Function

### Option A — AWS Console (Easiest for Beginners)
1. Go to **AWS Console → Lambda → Create Function**
2. Choose **"Author from scratch"**
3. Runtime: **Python 3.12**
4. Paste the code from this folder
5. Set the **IAM Role** with permissions for S3 and Connect

### Option B — AWS CLI
```bash
# Zip the file first
zip customer_lookup.zip customer_lookup.py

# Deploy using CLI
aws lambda create-function \
  --function-name CustomerLookup \
  --runtime python3.12 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/LambdaConnectRole \
  --handler customer_lookup.lambda_handler \
  --zip-file fileb://customer_lookup.zip
```

## Required IAM Permissions
Your Lambda execution role needs:
- `AmazonS3FullAccess` (for call_logger)
- `AmazonConnectReadOnlyAccess`
- `AWSLambdaBasicExecutionRole` (for CloudWatch logs)
