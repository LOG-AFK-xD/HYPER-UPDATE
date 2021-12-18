import os
from pyrogram import Client, filters
from pyrogram.types import *

from NaoRobot.conf import get_str_key
from NaoRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/cab6825dea9263d347831.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [Harsh](t.me/Harsh_Pandit) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @Harsh_Pandit_XD «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ Rᴇᴘᴏꜱɪᴛᴏʀʏ🔥", url=f"https://t.me_Proud_of_indian"),
        InlineKeyboardButton(" Jᴏɪɴ 💫", url=f"https://t.me/UNIQUE_SOCIETY"),
      ],[
        InlineKeyboardButton("Bot Oᴡɴᴇʀ ❣️", url="https://t.me/Log_AFK"),
        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/LOVE_X_POISON"),
      ],[
        InlineKeyboardButton("⚡ FRIEND ☑️", url="https://t.me/YASH_THAKUR_9"),
        InlineKeyboardButton("✌️ FRIEND ➡️", url="https://t.me/EVIL_BOY_XT"),
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
