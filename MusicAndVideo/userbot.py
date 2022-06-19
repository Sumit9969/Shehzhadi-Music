import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>😂 𝙿𝙾𝙽𝙶</b> `{delta_ping * 1000:.3f} ms` \n<b>⏳ 𝙰𝙲𝚃𝙸𝚅𝙴</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ ᴜsᴇʀʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>❤️ ʜᴇʟʟᴏ {m.from_user.mention}!

🛠  Hᴇʟᴘ Mᴇɴᴜ

» ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴇᴠᴇʀʏᴏɴᴇ

• {HNDLR}ᴘʟᴀʏ [sᴏɴɢ ᴛɪᴛᴇʟ|ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ| ʀᴇᴘʟʏ ᴀᴜᴅɪᴏ-ғɪʟᴇ] - Tᴏ ᴘʟᴀʏ ᴛʜᴇ sᴏɴɢ
• {HNDLR}ᴠᴘʟᴀʏ [ᴠɪᴅᴇᴏ ᴛɪᴛʟᴇ| ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ | ʀᴇᴘʟʏ ᴠɪᴅᴇᴏ ғɪʟᴇ] - ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ 
• {HNDLR}ᴘʟᴀʏʟɪsᴛ ᴛᴏ ᴠɪᴇᴡ ᴠɪᴅᴇᴏ 
• {HNDLR}ᴘɪɴɢ - ᴛᴏ ᴄʜᴇᴄᴋ sᴛᴀᴛᴜs
• {HNDLR}ʜᴇʟᴘ - ᴛᴏ ᴠɪᴇᴡ ᴀ ʟɪsᴛ ᴏғ ᴄᴏᴍᴍᴀɴᴅ

»ᴄᴏᴍᴍᴀɴᴅs ᴅᴏʀ ᴀʟʟ ᴀᴅᴍɪɴs

• {HNDLR}ʀᴇsᴜᴍᴇ - ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ᴘʟᴀʏɪɴɢ ᴛʜᴇ sᴏɴɢ ᴏʀ ᴠɪᴅᴇᴏ 
• {HNDLR}ᴘᴀᴜsᴇ - ᴛᴏ ᴘᴀᴜsᴇ ᴛʜᴇ ᴘʟᴀʏʙᴀᴄᴋ ᴏғ ᴀ sᴏɴɢ ᴏʀ ᴠɪᴅᴇᴏ 
• {HNDLR}sᴋɪᴘ - ᴛᴏ sᴋɪᴘ ᴀ sᴏɴɢ ᴏʀ ᴠɪᴅᴇᴏ 
• {HNDLR}ᴇɴᴅ - ᴛᴏ ᴇɴᴅ ᴘʟᴀʏʙᴀᴄᴋ </b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo", "sumit", "openbaby"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>❤️ ʜᴇʟʟᴏ {m.from_user.mention}!
      ✪ 🆂︎ʜᴇʜᴢʜᴀᴅɪ 🅼︎ᴜsɪᴄ ✪

 ᴛᴇʟᴇɢʀᴀᴍ Usᴇʀʙᴏᴛ ᴛᴏ ᴘʟᴀʏ sᴏɴɢs ᴀɴᴅ ᴠɪᴅᴇᴏs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ sᴜᴍɪᴛ ʏᴀᴅᴀᴠ.

»  sᴜʙsᴄʀɪʙᴇ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ
• [ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ](https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw)
• [ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ](https://t.me/TechQuard)


»  ✪ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ✪
 • ғɪʀsᴛ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛʜᴇɴ ᴛʏᴘᴇ #Shehzhadi-Music-Userbot
» sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ || [ᴛᴇᴄʜ ǫᴜᴀʀᴅ sᴜᴘᴘᴏʀᴛ](https://t.me/TechQuardSupport) 
 
 </b>
"""
    await m.reply(REPO, disable_web_page_preview=True, 
                  reply_markup=InlineKeyboardMarkup([
                      [InlineKeyboardButton("✨ Join Channel ✨", url=https://t.me/HEPPYLIFI)] 
                  ]
                  )
                 )
