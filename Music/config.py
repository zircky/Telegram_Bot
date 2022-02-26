import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Music YT AM BOT")
API_ID = int(getenv('API_ID', "15504206"))
API_HASH = getenv('API_HASH', '03f4b8c0e66ac848c56e4b730c8af98b')
MONGO_DB_URL = getenv("MONGO_DB_URL", "")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ''))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SUPERIOR_BOTS")
ZAID_SUPPORT = getenv("ZAID_SUPPORT", "SUPERIOR_SUPPORT")
ASS_ID = int(getenv("ASS_ID", ''))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))

BOT_USERNAME = getenv("BOT_USERNAME", "MusicYTBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zircky")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "MusicYTGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MusicYTProject")
OWNER_NAME = getenv("OWNER_NAME", "Badboyanim")
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")