from dotenv import load_dotenv
import os

db_host = '188.242.92.24'
db_user = 'postgres'
db_password = 'root'
db_name = 'postgres'

# webhook settings
WEBHOOK_HOST = 'https://vps443343.cloudfox.online'
WEBHOOK_PATH = '/webhook'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '188.242.92.24'  # or ip
WEBAPP_PORT = 5000


def get_fromenv(key):
    dotenv_path = 'config/.env'
    load_dotenv(dotenv_path)
    return os.environ.get(key)