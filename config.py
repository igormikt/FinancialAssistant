import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
EXCHANGE_RATE_API_URL = os.getenv('EXCHANGE_RATE_API_URL')
EXCHANGE_RATE_API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')