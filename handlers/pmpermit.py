from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is a music assistant service .\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **BHAK ONLY FOR ANIME MATRIX.**\n\n ⚠️ Disclamer: If you are sending a message here it means you are a nub\n    - Don't add this user to secret groups.\n   - Don't Share private info here\n\n **FEEL FREE TO CONTACT US @AnimeGroupMatrix**")
  return                        
