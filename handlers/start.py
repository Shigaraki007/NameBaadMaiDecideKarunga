from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n ♦️ Hello I'm Anime Matrix's VC Bot I can play music in Anime Matrix's group's voice chat 🎵 [🎵](https://telegra.ph/file/199b970849c5c4dd840e1.mp4")
🔆 I'm here for your service 
\n ⚡ You can't add me in your groups , please contact my master at Support Group first.
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤴My Master", url="https://t.me/DegenerateUSER",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/AnimeGroupMatrix"
                    ),
                    InlineKeyboardButton(
                        "🔊 My Channel", url="https://t.me/Download_Animes"
                    ),
                    InlineKeyboardButton(
                        "📚 Loges", url="https://t.me/AnimeGroupMatrix/1624"
                    ),
                ],
                [
                
                    InlineKeyboardButton(
                        "💾 Source code", url="https://t.me/AnimeGroupMatrix/30676"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/AnimeGroupMatrix/125847"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "🔍 Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/DownloadOngoing"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ecchi_Animee"
                    )
                ]
            ]
        )
    )    
