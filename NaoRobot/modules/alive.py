import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NaoRobot.events import register as MEMEK
from NaoRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/70242b21dc297e8b9436b.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  NAO = f"**Hello, I'm HYPERMEN ROBOT!** \n\n"
  NAO += "๐ด **I'm Working Properly** \n\n"
  NAO += "๐ด **My Master : [๐๐๐ ๐๐๐](https://t.me/Log_AFK)** \n\n"
  NAO += f"๐ด **Telethon Version : {tlhver}** \n\n"
  NAO += f"๐ด **Pyrogram Version : {pyrover}** \n\n"
  NAO += "**Thanks For Adding Me Here โค๏ธ**"
  BUTTON = [[Button.url("๐Sแดแดแดแดสแดโ๏ธ", "https://t.me/UNIQUE_SOCIETY"), Button.url("Pแดแดกแดสแดแด Bส", "https://t.me/EVIL_XD_BOY")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=NAO,  buttons=BUTTON)
