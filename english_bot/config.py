import os
from dotenv import load_dotenv

datebase_name = "english_bot_database.db"
load_dotenv()
'''instead of "os.getenv("token")" u can use token="your_token" or u can add '.env' file with token="your_token" and put into the root od the project'''
token=os.getenv("token")
