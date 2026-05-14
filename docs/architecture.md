# 🏗️ Architecture Overview

## System Design

This project implements a **cloud-native contact centre** on AWS.
Below is the detailed flow of how a customer interaction works end-to-end.

---

## Call Flow — Step by Step

```
1. Customer dials the phone number
         │
         ▼
2. Amazon Connect receives the call
   → Contact Flow starts executing
         │
         ▼
3. Lambda: CustomerLookup runs
   → Identifies the caller by phone number
   → Returns: Name, Account Number, Status
         │
         ├─── If known customer ──────────────────────┐
         │                                             │
         ▼                                             ▼
4a. Amazon Lex Bot greets:               4b. New customer flow:
    "Hello Riya! How can I help?"            "Welcome! Let me connect
                                              you to our team."
         │
         ▼
5. Customer states their query
   → Lex identifies the intent
   → Routes to the correct queue:
     • General Support Queue
     • Billing Support Queue
     • Technical Support Queue
         │
         ▼
6. Agent picks up the call
   → Agent screen shows customer info (via Lambda data)
         │
         ▼
7. Call ends
   → Lambda: CallLogger saves call record to S3
   → CloudWatch records all metrics
```

---

## AWS Services — Detailed Roles

### Amazon Connect
- Creates and manages the phone number
- Runs **Contact Flows** (visual logic builder — like a flowchart for calls)
- Manages **Queues** — waiting rooms for customers
- Manages **Routing Profiles** — controls which queue an agent handles
- Manages **Agent Users** — call centre staff accounts

### AWS Lambda
| Function | Trigger | Purpose |
|---|---|---|
| `CustomerLookup` | During call (Invoke Lambda block in Contact Flow) | Fetch customer info |
| `CallLogger` | After call ends (Kinesis CTR stream) | Log call data to S3 |

### Amazon Lex
- Understands natural language
- Maps spoken/typed phrases to **Intents** (e.g., "check my account")
- Extracts **Slots** (pieces of info, like account numbers)
- Embedded directly inside Amazon Connect Contact Flows

### Amazon S3
- Stores call logs as JSON files
- Folder structure: `call-logs/YYYY-MM-DD_HH-MM-SS_ContactID.json`
- Can also store call recordings (enabled in Connect settings)

### Amazon CloudWatch
- Collects metrics from Connect, Lambda, and Lex automatically
- Custom dashboard shows real-time stats
- Alarms send email alerts via SNS when thresholds are breached

### AWS IAM
- Lambda has an **Execution Role** with only the permissions it needs
- Principle of Least Privilege: each service only gets what it requires

---

## Key Design Decisions

| Decision | Reason |
|---|---|
| Python for Lambda | Simple, beginner-friendly, great AWS SDK (boto3) |
| JSON for config files | Easy to read, version-controlled, importable to AWS |
| GitHub Actions for CI/CD | Free for public repos, integrates with AWS easily |
| ap-south-1 (Mumbai) region | Low latency for India-based contact centre |
