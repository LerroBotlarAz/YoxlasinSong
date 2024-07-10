from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from bot.translate import EN

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "👨‍👩‍👧‍👦 XezerFamily", url="https://t.me/XezerFamily"
            ),
            InlineKeyboardButton("🤖 XezerBots", url="https://t.me/XezerBots"),
        ],
        [
            InlineKeyboardButton("👤 Owner", url="https://t.me/xGuliyev"),
        ],
        [
            InlineKeyboardButton(
                "📂 OpenSource", url="https://github.com/xGuliyev/MusicBot"
            ),
        ],
    ]
)


@Client.on_message(filters.command("start") & filters.private)
async def start(_, message: Message):
    await message.reply_text(
        text=EN.START_WELCOME,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=buttons,
    )
