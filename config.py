import os
from dotenv import load_dotenv

load_dotenv()

TG_API_KEY = os.getenv("TG_API_KEY")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")
