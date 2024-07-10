import os

import pyfiglet
from aylak import get_keys
from colorama import Fore, Style, init
from pyrogram import Client, idle

from bot import *
from config import *

API_HASH, API_ID = get_keys()

app = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot.plugins"),
)

if __name__ == "__main__":
    app.start()
    uname = app.get_me().username
    os.system("cls" if os.name == "nt" else "clear")
    uname_fig = pyfiglet.figlet_format(uname)
    print(f"{Fore.GREEN}{uname_fig}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}@{uname} Started!{Style.RESET_ALL}")
    idle()
    app.stop()
    print(f"{Fore.RED}@{uname} Stopped!{Style.RESET_ALL}")
