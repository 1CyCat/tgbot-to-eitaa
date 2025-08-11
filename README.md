# tgbot-to-eitaa
# Tg-Bot to Eitaa Channel Forwarder  
**Version:** 1.0.0

This script automatically forwards text messages received by a Telegram bot to a channel or group in Eitaa.  
Communication with Telegram is handled via the Pyrogram library, and communication with Eitaa is done through its official API.

---

## Prerequisites
- Python 3.8 or higher  
- Required libraries: `pyrogram`, `requests`, `tgcrypto` (optional)  
- Telegram API ID and API Hash (obtain from [my.telegram.org](https://my.telegram.org))  
- Telegram bot token (create a bot using [@BotFather](https://t.me/BotFather))  
- Eitaa bot token and target chat ID (obtain from [eitaayar.ir](https://eitaayar.ir/))

---

## Installation
Install the required Python libraries with pip:  
```bash
pip install requests pyrogram tgcrypto


Configuration
Replace the following variables in the script with your own values:
api_id
api_hash
bot_token
TOKEN (Eitaa bot token)
CHAT_ID (Eitaa target chat ID)

Make sure to use a VPN or proxy to connect to Telegram if needed.

Running the script
bash
Copy
Edit
python main.py
Important Notes
This script only forwards text messages.

Keep your API keys and tokens private; consider using environment variables or a .env file.

Using a proxy or VPN might be necessary to avoid connection issues with Telegram.
