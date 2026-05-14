# 🤖 Amazon Lex — AI Chatbot

Amazon Lex powers the AI chatbot that handles customer queries **before** routing them to a human agent.

## What This Bot Does

```
Customer calls → Bot greets → Bot understands intent → Routes accordingly

Example:
  Customer: "Check my account status"
  Bot:      "Sure! What's your account number?"
  Customer: "ACC001"
  Bot:      [calls Lambda] → "Your account is Active."
```

## Intents (What the Bot Understands)

| Intent | Example phrases | Action |
|---|---|---|
| `CheckAccountStatus` | "Check my account", "Is my account active?" | Calls Lambda to fetch data |
| `RaiseComplaint` | "I have a problem", "File a complaint" | Routes to specialist queue |
| `TransferToAgent` | "Talk to an agent", "Speak to a human" | Transfers to live agent |
| `FallbackIntent` | Anything not understood | Transfers to agent with message |

## How to Create This Bot in AWS Console

1. Go to **Amazon Lex V2 → Create Bot**
2. Bot name: `ConnectSupportBot`
3. Language: **English (India)**
4. Add intents from `bot_config.json` manually
5. Build and test the bot in the console
6. **Integrate with Amazon Connect:**
   - Go to your Connect instance → Contact flows
   - Add a **"Get customer input"** block
   - Select Lex bot and choose `ConnectSupportBot`

## Tips for Beginners
- Start with just 1 intent (`TransferToAgent`) and test it
- Add more intents one at a time
- Always test in the Lex console before connecting to Amazon Connect
