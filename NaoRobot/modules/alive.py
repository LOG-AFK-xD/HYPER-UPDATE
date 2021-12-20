import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NaoRobot.events import register as MEMEK
from NaoRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/1b0bbf62e1c6a2d9886dc.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  NAO = f"**Hello, I'm HYPERMEN Robot!** \n\n"
  NAO += "🔴 **I'm Working Properly** \n\n"
  NAO += "🔴 **My Master : [Harsh](https://t.me/Harsh_Pandit)** \n\n"
  NAO += f"🔴 **Telethon Version : {tlhver}** \n\n"
  NAO += f"🔴 **Pyrogram Version : {pyrover}** \n\n"
  NAO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Hypermen_rbot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/UNIQUE_SOCIETY")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=NAO,  buttons=BUTTON)
