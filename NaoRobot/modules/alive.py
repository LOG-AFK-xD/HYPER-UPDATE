import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NaoRobot.events import register as MEMEK
from NaoRobot import telethn as tbot


@MEMEK(pattern=("/Hello"))
async def awake(event):
  tai = event.sender.first_name
  NAO = f"**╔┓┏╦━╦┓╔┓╔━━╗
║┗┛║┗╣┃║┃║X X║
║┏┓║┏╣┗╣┗╣╰╯║
╚┛┗╩━╩━╩━╩━━╝**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Hypermen_rbot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/UNIQUE_SOCIETY")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=NAO,  buttons=BUTTON)
