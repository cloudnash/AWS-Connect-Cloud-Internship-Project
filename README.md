# ☁️ AWS Connect Cloud Internship Project

> **Role:** Cloud Intern — Amazon Connect & AWS Services  
> **Goal:** Build a beginner-friendly, production-style cloud contact centre solution using core AWS services.

---

## 📌 Project Overview

This project simulates a real-world **cloud contact centre** built on **Amazon Connect**, integrated with key AWS services. It covers everything from routing customer calls to AI-powered chatbots, automated workflows, and live monitoring dashboards.

Built as a **learning showcase** — simple enough for beginners, structured for professionals.

---

## 🏗️ Architecture Diagram

```
Incoming Call / Chat
        │
        ▼
 ┌─────────────────┐
 │  Amazon Connect  │  ◄──── Contact Flows, Queues, Routing Profiles
 └────────┬────────┘
          │
    ┌─────┴──────┐
    │            │
    ▼            ▼
Amazon Lex    AWS Lambda
(AI Chatbot)  (Custom Logic)
                  │
                  ▼
             Amazon S3
           (Call Logs / Data)
                  │
                  ▼
        Amazon CloudWatch
        (Monitoring & Alerts)
```

---

## 📁 Project Structure

```
aws-connect-internship/
│
├── 📂 lambda/                  # AWS Lambda functions (Python)
│   ├── customer_lookup.py      # Fetch customer info from database
│   ├── call_logger.py          # Log call data to Amazon S3
│   └── README.md
│
├── 📂 lex-bot/                 # Amazon Lex chatbot configuration
│   ├── bot_config.json         # Bot intents and slots definition
│   └── README.md
│
├── 📂 monitoring/              # CloudWatch dashboards & alerts
│   ├── cloudwatch_dashboard.json
│   ├── alarm_config.json
│   └── README.md
│
├── 📂 scripts/                 # Automation & utility scripts
│   ├── setup_connect.py        # Automate Connect instance setup
│   ├── create_queues.py        # Create queues via AWS SDK (boto3)
│   └── README.md
│
├── 📂 docs/                    # Documentation & user guides
│   ├── architecture.md
│   ├── setup-guide.md
│   └── contact-flow-guide.md
│
├── 📂 .github/workflows/       # CI/CD pipeline (GitHub Actions)
│   └── deploy.yml
│
└── README.md                   ← You are here
```

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| **Amazon Connect** | Core contact centre — calls, chat, routing |
| **AWS Lambda** | Serverless functions for custom logic |
| **Amazon Lex** | AI chatbot for automated customer interactions |
| **Amazon S3** | Store call recordings and logs |
| **Amazon CloudWatch** | Monitor metrics, set alarms, view dashboards |
| **AWS IAM** | Manage permissions and access roles |
| **AWS SDK (boto3)** | Python library to interact with all AWS services |

---

## 🚀 Getting Started

### Prerequisites
- AWS Account (Free Tier works)
- Python 3.9+
- AWS CLI installed and configured
- Basic understanding of cloud concepts

### Step 1 — Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/aws-connect-internship.git
cd aws-connect-internship
```

### Step 2 — Install Dependencies
```bash
pip install boto3 python-dotenv
```

### Step 3 — Configure AWS Credentials
```bash
aws configure
# Enter your: Access Key, Secret Key, Region (e.g. ap-south-1)
```

### Step 4 — Run Setup Script
```bash
python scripts/setup_connect.py
```

---

## 📚 Learning Outcomes

- ✅ Set up Amazon Connect contact flows and queues
- ✅ Integrate Lambda functions with Amazon Connect
- ✅ Build an Amazon Lex AI chatbot and connect it to a flow
- ✅ Store and retrieve call data using Amazon S3
- ✅ Monitor infrastructure with CloudWatch dashboards and alarms
- ✅ Automate deployments using GitHub Actions CI/CD

---

## 🤝 Contributing

This is an internship learning project. Feel free to fork, explore, and learn from it!

---

*📞 Contact*
---

- GitHub: [@cloudnash](https://github.com/cloudnash)
- LinkedIn: [Nashit Ahmad](https://in.linkedin.com/in/nashitahmad)
- Email: nashitakerfeldt@gmail.com

---
