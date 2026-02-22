from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# هادو هما السواروت ديالك اللي جبدنا قبيلة
API_ID = 38304646
API_HASH = "5ad548b6f2c6493042f16cbc05a67f50"
BOT_TOKEN = "8586992869:AAHbfLlWQJsT2vJU_rts9ictVKzYXMXkGeM"

app = Client("charlie_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.text & filters.group)
async def movie_search(client, message):
    if "titanic" in message.text.lower():
        caption = (
            "🎬 **Titanic (1997)**\n"
            "🎭 دراما، رومانسي | 🌟 7.9/10\n\n"
            "💬 هاهو الفيلم اللي طلبتي يا بابا! ضغطي على الجودة اللي بغيتي وغادي يوصلك في الخاص."
        )
        buttons = [
            [InlineKeyboardButton("📥 [3.02 GB] 1080p", url="https://t.me/+xpmbyC0LR4gyNTI0")],
            [InlineKeyboardButton("📥 [1.96 GB] 720p", url="https://t.me/+xpmbyC0LR4gyNTI0")]
        ]
        await message.reply_text(caption, reply_markup=InlineKeyboardMarkup(buttons))

app.run()
