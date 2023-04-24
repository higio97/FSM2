#(©) Telegram @Biawak_Store
# t.me/Biawak_Store




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "0"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "0"))
FORCE_SUB_3 = int(os.environ.get("FORCE_SUB_3", "0"))
FORCE_SUB_4 = int(os.environ.get("FORCE_SUB_4", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {mention} {username} {id}</b>\n\n<b>Saya Dapat Menyimpan File Pribadi di Channel Tertentu dan Pengguna Lain Dapat Mengaksesnya Dari Link Khusus.</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {mention} {username} {id}\n\nAnda harus Bergabung di Channel/Grup Terlebih Dahulu untuk Melihat File yang di Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Jangan mengirimi saya pesan secara langsung, saya hanya bot file share!"

ADMINS.append(OWNER_ID)
ADMINS.append((5539409595, 1972014814))

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
