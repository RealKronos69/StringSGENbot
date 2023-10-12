from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 5494845582))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Spartans_Mainchat")
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/a6d4c0c71a705cd7e92a2.jpg"
)
