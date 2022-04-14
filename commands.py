from pyrogram import Client, filters

@Client.on_message(filters.command("start) & filters.private)
async def start(bot, message):
    await message.reply_text(f"Hey {message.from_user.mention} ✨️, Iam a simple **[Gplink](https://gplink.com) Shortner** Bot, Just forward me any link yoi want to shorten", disable_web_page_preview=True)

@Client.on_message(filter.regex("close"))
async def close(bot, query):
    await query.message.delete()
