from dotenv import load_dotenv
import os

load_dotenv()



# project secrets loading form  .env

DEBUG = os.getenv('DEBUG', 'False')

SECRET_KEY = os.getenv('SECRET_KEY',"")

DB_NAME = os.getenv('DB_NAME')

DB_USER_NAME = os.getenv("DB_USER_NAME")

DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_HOST = os.getenv("DB_HOST")

DB_PORT = os.getenv("DB_PORT",5482)
