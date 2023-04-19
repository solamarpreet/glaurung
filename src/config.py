import os
from dotenv import load_dotenv

try:
    load_dotenv()
except:
    load_dotenv("../.env")

def get_openai_token():
    return os.getenv("OPENAI_TOKEN")

def get_discord_token():
    return os.getenv("DISCORD_TOKEN")
