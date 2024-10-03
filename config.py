from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

USE_WEBHOOK = os.getenv('USE_WEBHOOK').lower() == 'true'
WEBHOOK_HOST = os.getenv('RAILWAY_PRIVATE_DOMAIN')
WEBHOOK_PORT = os.getenv('PORT', default=5000)
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
