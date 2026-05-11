import os
from pyrogram import Client, filters

API_ID = int(os.environ.get("31807122"))
API_HASH = os.environ.get("18918325e19aa86c3c8bc4f7cf1574e0")
BOT_TOKEN = os.environ.get("8777730859:AAFzkSiXraVOqwy8kJ6gFLKSILqtwoUVQC4")

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.private & filters.text)
async def start(client, message):
    await message.reply("البوت شغال 🚀")

print("Bot running...")
app.run()
