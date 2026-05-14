# ⚙️ Automation Scripts

Python scripts to automate AWS resource setup using **boto3** (AWS SDK for Python).

## Scripts

| Script | What it does |
|---|---|
| `setup_connect.py` | Creates Amazon Connect instance + queues |

## Prerequisites
```bash
pip install boto3 python-dotenv
aws configure  # make sure your credentials are set
```

## Running
```bash
# From the project root
python scripts/setup_connect.py
```

## Output
Creates a `connect_config.json` file with your instance ID and queue IDs.
Save this — you'll need the instance ID for Lex and Lambda integration.

## Beginner Tip 💡
`boto3` is the official AWS Python library. It lets you control ANY AWS service from Python code.
The pattern is always the same:
```python
import boto3
client = boto3.client("SERVICE_NAME", region_name="REGION")
response = client.some_action(...)
```
