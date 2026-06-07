import os
import sqlite3
import requests
import logging
from telethon import TelegramClient, events, Button

# Railway থেকে এনভায়রনমেন্ট ভেরিয়েবল নেওয়া
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

MY_NUMBER = "01824297780" 
BRAND_KEY = "WEMZNXQVhgaHf0QMqsV2FwIvlUg50Yt7thNHcRQrrhj1uUJZCc"

# ডাটাবেস সেটআপ
conn = sqlite3.connect("oggy_auto_shop.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS panel_keys (
                    key_text TEXT PRIMARY KEY, 
                    product_tag TEXT,
                    is_used INTEGER DEFAULT 0)''')
conn.commit()

bot = TelegramClient('oggy_auto_shop', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

main_menu_buttons = [
    [Button.inline("🎮 Select a Mod/Hack/Bot", b"view_categories")],
    [Button.inline("💬 Support / Contact Admin", b"contact_admin")]
]

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("👋 **Welcome to OGGY PREMIUM SHOP!**\n\nআমাদের অটোমেটেড শপে স্বাগতম।", buttons=main_menu_buttons)

@bot.on(events.CallbackQuery)
async def callback_handler(event):
    data = event.data
    if data == b"view_categories":
        buttons = [
            [Button.inline("🛡️ HG CHEST", b"cat_hg_chest"), Button.inline("🦆 PATO TEAM", b"cat_pato")],
            [Button.inline("⬅️ Back", b"back_to_main")]
        ]
        await event.edit("👇 **ক্যাটাগরি সিলেক্ট করুন:**", buttons=buttons)
    
    elif data == b"back_to_main":
        await event.edit("👋 **Welcome to OGGY PREMIUM SHOP!**", buttons=main_menu_buttons)
        
    elif data == b"contact_admin":
        await event.respond("💬 যোগাযোগ করুন: @soheladnan2")
        await event.answer()

print("🤖 OGGY AUTO-PAY SHOP BOT IS ONLINE...")
bot.run_until_disconnected()
