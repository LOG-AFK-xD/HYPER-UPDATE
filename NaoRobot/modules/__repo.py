import os
from pyrogram import Client, filters
from pyrogram.types import *

from NaoRobot.conf import get_str_key
from NaoRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/f819b0e13c279ff09e69b.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [𝐋𝐎𝐆 𝐀𝐅𝐊](t.me/LOG_AFK) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @THE_FURIOUSNETWORK «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("📢Pᴏᴡᴇʀᴇᴅ Bʏ🔥", url=f"https://t.me/THE_FURIOUSNETWORK"),
        InlineKeyboardButton("✨Sᴜᴘᴘᴏʀᴛ💫", url=f"https://t.me/Furious_Support_Group"),
      ],[
        InlineKeyboardButton("✌️ Cʜᴀᴛ Gʀᴏᴜᴩ ❣️", url="https://t.me/LOVE_X_POISON"),
        InlineKeyboardButton("✨Cʜᴀᴛ Gʀᴏᴜᴘ 🔐", url="https://t.me/UNIQUE_SOCIETY"),
      ],[
        InlineKeyboardButton("❣️ Bʜᴀɪ ☑️", url="https://t.me/yash_thakur_9"),
        InlineKeyboardButton("❣️ Bʜᴀɪ ☑️", url="https://t.me/EVIL_XD_BOY"),
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
