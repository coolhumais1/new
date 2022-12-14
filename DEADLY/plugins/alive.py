import os
import sys
import asyncio
from time import time
from datetime import datetime
from pyrogram import filters
from sys import version_info
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import __version__ as pversion
from resources.data import PROGROUPS, DEV
from DEADLY import ALIVE_PIC, SUDOERS



START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)




pthversion = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"




@Client.on_message(filters.user(SUDOERS) & filters.command(["alive", "on", "start"], [".", "!", "/", ",", "+", "?"]))
async def alive(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))  
    ALIVE_TXT = f"ɴᴏᴏʙ sᴘᴀᴍ ᴜsᴇʀʙᴏᴛ 🇮🇳\n"
    ALIVE_TXT += f"🔸**ʏᴏᴜʀ ᴅᴇᴀᴅʟʏsᴘᴀᴍ ɪs 𝟷𝟶𝟶% sᴀғᴇ ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ**\n\n"
    ALIVE_TXT += f"🔹 **ᴛʜɪs ᴜsᴇʀʙᴏᴛ ɪs 100% ᴍᴀᴅᴇ ᴡɪᴛʜ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ sᴀғᴇ**\n\n"
    ALIVE_TXT += f"════════════════════\n"
    ALIVE_TXT += f"🔸 ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ: {pversion}\n"
    ALIVE_TXT += f"🔹 ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {pthversion}\n"
    ALIVE_TXT += f"🔸 ᴜᴘᴛɪᴍᴇ {uptime} ᴘɪɴɢ {delta_ping * 1000:.3f}ᴍs\n\n"
    ALIVE_TXT += f"════════════════════\n"
    ALIVE_TXT += f"🔸[sᴜᴘᴘᴏʀᴛ](https://t.me/noobcreator)🔹|🔸[ᴄʜᴀɴɴᴇʟ](https://t.me/noobxcreator)\n"
    await m.delete() 
    await m.reply_photo(photo=ALIVE_PIC, caption=ALIVE_TXT) 


@Client.on_message(filters.user(SUDOERS) & filters.command(["ping", "pong"], [".", "!", "/", ",", "+", "?"]))
async def ping(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    delta_ping = time() - start
    ping_a = "▒█▀▀█ ▀█▀ ▒█▄░▒█ ▒█▀▀█\n▒█▄▄█ ▒█░ ▒█▒█▒█ ▒█░▄▄\n▒█░░░ ▄█▄ ▒█░░▀█ ▒█▄▄█\n\n"  
    ping_b = f"ᴘᴏɴɢ ᴍᴀᴅᴇ ʙʏ @PiRoKiD:🏓 {delta_ping * 1000:.3f}ᴍs\n"
    text = f"{ping_a} {ping_b}"
    await m.delete() 
    await m.reply_text(text) 
 

@Client.on_message(filters.user(SUDOERS) & filters.command(["help", "cmds"], [".", "!", "/"]))
async def eqw(client: Client, m: Message):
    blaze = await m.reply_text("Processing...")
    help_a = f"🔥ɴᴏᴏʙ sᴘᴀᴍ ᴜsᴇʀʙᴏᴛ🔥\n\n"
    help_a += f"ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɴᴏᴏʙ sᴘᴀᴍ ᴄᴍɴᴅs ʜᴇʟᴘ\n\n"
    help_a += f"🔸 ᴅᴍ ᴄᴍɴᴅs 🚀\n\n"
    help_a += f".dm [username] [msz]\n"
    help_a += f".draid [count]  [username/reply_to_user]\n\n"
    help_a += f"🔹 ʀᴀɪᴅ ᴄᴍɴᴅs 🚀\n\n"
    help_a += f".raid [count] [username/reply_to_user]\n"
    help_a += f".replyraid [username/reply_to_user]\n"
    help_a += f".dreplyraid [username/reply_to_user]\n\n"
    help_a += f"🔸 ᴇᴄʜᴏ ᴄᴍɴᴅs 🚀\n\n"
    help_a += f".addecho [username/reply_to_user]\n"
    help_a += f".rmecho [username/reply_to_user]\n\n"
    help_a += f"🔹 ʙᴏᴛ ᴄᴍɴᴅs 🚀\n\n"
    help_a += f".alive to check if alive\n"
    help_a += f".ping to check ping\n"
    help_a += f".restart to restart bot\n\n"
    help_a += f"🔸 sᴘᴀᴍ ᴄᴍɴᴅs 🚀\n\n"
    help_a += f".spam [count] [spam_text]\n"
    help_a += f".delayspam [sleep time] [count] [message to spam]\n\n"
    help_a += f"🔹 ᴍᴀɴᴀɢᴇᴅ ʙʏ: @WARIORNETWORK\n"
    await m.delete() 
    await blaze.edit(help_a) 
