from pyrogram import Client, filters
from config import API_ID, API_HASH, TG_BOT_TOKEN

class GPLink(object):
  def __init__(self):
    super().__init__(
      "GPlink bot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=TG_BOT_TOKEN,
    )
    
    async def start_gp(self):
      super().start_gp()
      print("Bot has been started")
      
    async def stop_gp(self):
      super().stop_gp()
      print("Bot stopped.Bye")

  
