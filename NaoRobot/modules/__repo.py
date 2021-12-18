import os
from pyrogram import Client, filters
from pyrogram.types import *

from NaoRobot.conf import get_str_key
from NaoRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/f819b0e13c279ff09e69b.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [𝗛𝗮𝗿𝘀𝗵](t.me/Harsh_Pandit) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @Harsh_Pandit_XD «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("💫Rᴇᴘᴏꜱɪᴛᴏʀʏ🔥", url=f"https://me/Log_Afk"),
        InlineKeyboardButton("✨Cʜᴀᴛ Gʀᴏᴜᴘ💫", url=f"https://t.me/LOVE_X_POISON"),
      ],[
        InlineKeyboardButton("✌️ Oᴡɴᴇʀ ❣️", url="https://t.me/PROUD_OF_INDIAN"),
        InlineKeyboardButton("✨Sᴜᴘᴘᴏʀᴛ 🔐", url="https://t.me/UNIQUE_SOCIETY"),
      ],[
        InlineKeyboardButton("❣️ Bʜᴀɪ ☑️", url="https://t.me/Yash_Thakur_9"),
        InlineKeyboardButton("❣️ Bʜᴀɪ ➡️", url="https://t.me/EVIL_BOY_XT"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
