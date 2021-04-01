from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
Grubunuzun sesli sohbetinde müzik çalmanıza izin 😉
Şu anda desteklediğim komutlar şunlardır:
⚜️ /play - yanıtlanan ses dosyasını veya YouTube videosunu link.__ aracılığıyla __Plays
⚜️ /pause - Sesli Sohbet Music.__ __Pause
⚜️ /resume - sesli sohbet Music.__ __Resume
⚜️ /skip - Geçerli Ses Chat.__ Çalan Müzik __Skips
⚜️ /stop - Sırayı __Clears ve Sesli Sohbet Müziği'ni sonlandırın.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group 💬", url="https://t.me/OlympusCh4t"
                    ),
                    InlineKeyboardButton(
                        "Channel 📣", url="https://t.me/WylineVoiceHelp"
                    )
                ]
            ]
        )
    )
