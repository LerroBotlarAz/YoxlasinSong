from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class EN:
    START_WELCOME = "🎶 Hello! I'm a simple Telegram bot.\n🤖 That can download songs for you.\n🎵 Just send me the name of the song you want to download, and I'll do the rest. 🚀"

    SONG_SEARCHING = "🔄 Searching... **"
    SONG_NOT_FOUND = (
        "⚠️ No results were found. Make sure you typed the correct song name."
    )
    SONG_DOWNLOADING = "📥 Downloading..."
    SONG_UPLOADING = "📤 Uploading..."
    SONG_SEND_SONG = "{}\nRequested by: {}\nChannel: {}"
    SONG_ERROR = "Error: Try again later."
    SONG_SEND_FAILED = "Failed to send the song."

    START_BUTTONS = InlineKeyboardMarkup(
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

    SONG_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "👨‍👩‍👧‍👦 XezerFamily", url="https://t.me/XezerFamily"
                )
            ],
        ]
    )
