# (©) Telegram @Biawak_Store
# t.me/Biawak_Store

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 └ /help - Bantuan Perintah Bot ini 
 
 ❏ Perintah Untuk Admin BOT
 ├ /users - Untuk Melihat Statistik Pengguna Bot
 ├ /batch - Untuk Membuat Link Lebih dari Satu File
 ├ /stats - Untuk Melihat Status Bot 
 └ /broadcast - Untuk Mengirim Pesan Broadcast ke Pengguna Bot

👨‍💻 Develoved by <a href='https://t.me/Biawak_Store'>@Biawak_Store</a></b>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram Untuk Menyimpan File Yang Dapat Diakses Melalui Link Khusus.

 • Creator: @{}

👨‍💻 Develoved by <a href='https://t.me/Biawak_Store'>@Biawak_Store</a></b>
"""
