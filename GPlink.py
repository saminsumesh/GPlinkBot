import aiohttp
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
from config import API_ID, API_HASH, TG_BOT_TOKEN, API_KEY


client = Client(
    "Gplink bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TG_BOT_TOKEN
   )

@client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    await message.reply_text(f"Hey {message.from_user.mention} ✨️, Iam a simple **[Gplink](https://gplinks.in) Shortner** Bot, Just forward me any link yoi want to shorten", disable_web_page_preview=True)

@client.on_message(filters.regex("close"))
async def close(bot, query):
    await query.message.delete()


@client.on_message(filters.regex(r"https:?//[^\s]+") & filters.private)
async def link_handler(client, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply_text(
            text="Here is your shortened link",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Short Link", url=f"{short_url}")
                                              ],[
                                                InlineKeyboardButton("Close", callback_data="close")
                                              ]]))
    except Exception as e:
        print(e)
        await message.reply_text(f"There was an error {e}", quote=True)

async def get_shortlink(link):
    url = "https://gplinks.in/api"
    params = {"api": API_KEY, "url": link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedurl"]


client.run()
