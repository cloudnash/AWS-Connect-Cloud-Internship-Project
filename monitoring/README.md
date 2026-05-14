# 📊 Monitoring & Alerts

This folder contains configuration for the CloudWatch monitoring setup.

## Dashboard Metrics

| Metric | Why It Matters |
|---|---|
| Calls in Queue | High = customers waiting too long → need more agents |
| Average Handle Time | Measures agent efficiency |
| Missed/Abandoned Calls | Customers who gave up — impacts customer satisfaction |
| Lambda Errors | Code failures that affect call quality |

## Alarms

| Alarm | Threshold | Action |
|---|---|---|
| HighCallsInQueue | > 10 callers waiting | Email alert via SNS |
| LambdaErrorsHigh | > 5 errors in 5 mins | Email alert via SNS |

## How to Import Dashboard

```bash
aws cloudwatch put-dashboard \
  --dashboard-name ConnectContactCentreDashboard \
  --dashboard-body file://cloudwatch_dashboard.json
```

## How to Create an Alarm

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name HighCallsInQueue \
  --metric-name CallsInQueue \
  --namespace AWS/Connect \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --period 60 \
  --statistic Maximum \
  --alarm-actions arn:aws:sns:ap-south-1:YOUR_ACCOUNT_ID:ConnectAlerts
```
