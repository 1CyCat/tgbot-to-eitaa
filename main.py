from pyrogram import Client, filters
import requests

# define the proxy
proxy_host = "127.0.0.1"
proxy_port = 1089
proxies = {
    'http': f'socks5h://{proxy_host}:{proxy_port}',
    'https': f'socks5h://{proxy_host}:{proxy_port}'
}

# check for proxy working(optional)
response = requests.get("https://ipinfo.io/json", proxies=proxies)
if response.status_code == 200:
    timezone = response.json().get("timezone", "❓ Unknown")
    print("- Area: ", timezone)
else:
    print("- Could not fetch country info.")
    country = "Unknown"

# paste your api-id & api-hash & token-bot
api_id = 12345678
api_hash = "aaaaaaaaaaaaaaaa1111111111111111"
bot_token = "aaaaaa1111:aaaa1111aaaa111aaa11aaa11a_aaaaaaaa"
app = Client(
    "test_session",
    api_id=api_id,
    api_hash=api_hash,
    bot_token= bot_token,
    proxy=dict(
        hostname=proxy_host,
        port=proxy_port,
        scheme="socks5"
    )
)


# eitaa token & chat-id
TOKEN = "bot221a21:aaa1111a-1111-111a-a11a-aaaa1111a1a1"
CHAT_ID = "111111aa"
url = f"https://eitaayar.ir/api/{TOKEN}/sendMessage"



@app.on_message(filters.private & filters.text)
def forward_to_eitaa(client, message):
    text = message.text
    print(f"New Text from Tg-Bot received: [{text}]")
    
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("Message was sent succsesfully from Tg-Bot to target in eitaa")
    else:
        print("Sending message to Target was unsuccsesfull\n", response.text)

    

app.run()
