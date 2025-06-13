#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29410975"))
API_HASH = environ.get("API_HASH", "f7b94f03cb81efef112761048cb1b4b1")
BOT_TOKEN = environ.get("BOT_TOKEN", "7697011830:AAHNPJKSnQax8KG-Y-cksPbXsT1cj4WW_Cc")
OWNER = int(environ.get("OWNER", "7457390260"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '7457390260').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
