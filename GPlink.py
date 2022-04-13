from aiohttp import ClientSession
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import GPLink

client = GPLink()

@client.on_message(filter.regex(r"https:?//[^\s]=+") & filters.private)
async def url_handler(client, message):
    link = message.matches[0].group(0)
    try:
        short_url = await make_shorturl(link)
        await message.reply_text(
            text="Here is your shortened link",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Short Link", url=f"{short_url}"),
                                                InlineKeyboardButton("Close", callback_data="close")]])
            disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(f"There was an error {e}", qoute=True)

async def make_shorturl(link):
    url = "https://gplink.com/api"
    params = {"api":API_KEY, "url": link}

    async with ClientSession().get(url, params=params, raise_for_status=True) as response:
        data = await response.json()
        return data["shorturl"]


# I have used the same method of https://github.com/Mahesh0253/GPlink-bot to make the bot
# All credits goes to the respective owners
