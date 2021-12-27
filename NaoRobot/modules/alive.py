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
  NAO += "🔴 **I'm Working Properly** \n\n"
  NAO += "🔴 **My Master : [𝐋𝐎𝐆 𝐀𝐅𝐊](https://t.me/Log_AFK)** \n\n"
  NAO += f"🔴 **Telethon Version : {tlhver}** \n\n"
  NAO += f"🔴 **Pyrogram Version : {pyrover}** \n\n"
  NAO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("👆Sᴜᴘᴘᴏʀᴛ✌️", "https://t.me/UNIQUE_SOCIETE"), Button.url("Pᴏᴡᴇʀᴇᴅ Bʏ", "https://t.me/LOG_AFK")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=NAO,  buttons=BUTTON)
