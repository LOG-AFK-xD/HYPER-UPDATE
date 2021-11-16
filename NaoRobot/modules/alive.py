import re
import os

from telethon import events, Button
from telethon import version as tlhver
from pyrogram import version
from NaoRobot.events import register
from NaoRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/674bb34bc80e2a6aaa0b6.jpg"

@register(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  AKIRA = f"**Holla {tai}, I'm ᴀᴋɪʀᴀ ʀᴏʙᴏᴛ!** \n\n"
  AKIRA += "🔴 I'm Working Properly \n\n"
  AKIRA += "🔴 My Master : [ʟᴏʀᴅ](https://t.me/Bukan_guudlooking) \n\n"
  AKIRA += f"🔴 Telethon Version : {tlhver} \n\n"
  AKIRA += f"🔴 Pyrogram Version : {pyrover} \n\n"
  AKIRA += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Akiramanagerbot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/AkiraSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=SKYZU,  buttons=BUTTON)
