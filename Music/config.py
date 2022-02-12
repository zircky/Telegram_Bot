from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "15504206"))
API_HASH = getenv('API_HASH', '03f4b8c0e66ac848c56e4b730c8af98b')