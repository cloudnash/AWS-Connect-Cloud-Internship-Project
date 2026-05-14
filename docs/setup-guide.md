# 🛠️ Setup Guide — Step by Step

This guide walks you through setting up the entire project from scratch.
Designed for beginners with no prior AWS experience.

---

## Phase 1 — AWS Account Setup (One-Time)

### 1.1 Create an AWS Account
- Go to [aws.amazon.com](https://aws.amazon.com) → Create Account
- Free Tier is sufficient for this project
- Set up **MFA (Multi-Factor Authentication)** for security

### 1.2 Create an IAM User (Don't use root!)
1. AWS Console → **IAM → Users → Create User**
2. Username: `connect-intern`
3. Attach policies:
   - `AmazonConnectFullAccess`
   - `AWSLambdaFullAccess`
   - `AmazonS3FullAccess`
   - `AmazonLexFullAccess`
   - `CloudWatchFullAccess`
4. Download the **Access Key CSV** — save it safely!

### 1.3 Install AWS CLI
```bash
# macOS
brew install awscli

# Windows — download from:
# https://aws.amazon.com/cli/

# Verify
aws --version
```

### 1.4 Configure AWS CLI
```bash
aws configure
# AWS Access Key ID:     [paste from CSV]
# AWS Secret Access Key: [paste from CSV]
# Default region name:   ap-south-1
# Default output format: json
```

---

## Phase 2 — Amazon Connect Setup

### 2.1 Run the Setup Script
```bash
# From the project root
python scripts/setup_connect.py
```
This creates your Connect instance and 3 queues automatically.

### 2.2 Verify in Console
1. Go to **AWS Console → Amazon Connect**
2. Click your instance → **View Amazon Connect console**
3. You should see the 3 queues under Routing → Queues

---

## Phase 3 — Lambda Functions

### 3.1 Create S3 Bucket (for call logs)
```bash
aws s3 mb s3://my-connect-call-logs --region ap-south-1
```

### 3.2 Create Lambda Execution Role
1. AWS Console → **IAM → Roles → Create Role**
2. Trusted entity: **Lambda**
3. Attach: `AmazonS3FullAccess` + `AWSLambdaBasicExecutionRole`
4. Name it: `LambdaConnectRole`

### 3.3 Deploy Lambda Functions
```bash
# CustomerLookup
cd lambda
zip customer_lookup.zip customer_lookup.py
aws lambda create-function \
  --function-name CustomerLookup \
  --runtime python3.12 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/LambdaConnectRole \
  --handler customer_lookup.lambda_handler \
  --zip-file fileb://customer_lookup.zip

# CallLogger
zip call_logger.zip call_logger.py
aws lambda create-function \
  --function-name CallLogger \
  --runtime python3.12 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/LambdaConnectRole \
  --handler call_logger.lambda_handler \
  --zip-file fileb://call_logger.zip
```

---

## Phase 4 — Amazon Lex Bot

1. AWS Console → **Amazon Lex V2 → Create Bot**
2. Bot name: `ConnectSupportBot`
3. Language: English (India)
4. Refer to `lex-bot/bot_config.json` to add intents
5. Build the bot → Test it in the console

---

## Phase 5 — Monitoring

### Create CloudWatch Dashboard
1. AWS Console → **CloudWatch → Dashboards → Create**
2. Name: `ConnectContactCentreDashboard`
3. Add widgets using the metrics in `monitoring/cloudwatch_dashboard.json`

### Set Up Alarms
1. Create SNS topic: `ConnectAlerts`
2. Subscribe your email
3. Create alarms from `monitoring/alarm_config.json`

---

## Phase 6 — CI/CD with GitHub Actions

1. Push your code to GitHub
2. Go to **Settings → Secrets and variables → Actions**
3. Add:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
4. Push a change to the `lambda/` folder — the pipeline runs automatically!

---

## ✅ You're Done!

Your contact centre is now running on AWS with:
- ☎️ Amazon Connect handling calls
- 🤖 Lex bot handling AI interactions
- ⚡ Lambda functions processing data
- 🗄️ S3 storing call logs
- 📊 CloudWatch monitoring everything
- 🔄 GitHub Actions deploying code changes
