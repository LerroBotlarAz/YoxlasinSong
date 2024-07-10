import os
import time
from time import time

import requests
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtube_search import YoutubeSearch

from bot.translate import EN

buttons = EN.SONG_BUTTONS


@Client.on_message(filters.command("song"))
async def download_song(_, message):
    user_id = message.from_user.id
    current_time = time()
    query = " ".join(message.command[1:])
    print(query)
    m = await message.reply(EN.SONG_SEARCHING)
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        channel_name = results[0]["channel"]

    except Exception as e:
        await m.edit(EN.SONG_NOT_FOUND)
        print(str(e))
        return
    await m.edit(EN.SONG_DOWNLOADING)
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.edit(EN.SONG_UPLOADING)

        await message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=EN.SONG_SEND_SONG.format(
                title, message.from_user.mention, channel_name
            ),
            duration=dur,
            reply_markup=buttons,
        )
        await m.delete()
    except Exception as e:
        await m.edit(EN.SONG_ERROR)
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
