from pyrogram import Client, filters
from config import API_ID, API_HASH, TG_BOT_TOKEN

client = Client(
    "Gplink bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TG_BOT_TOKEN
   )


client.run()
