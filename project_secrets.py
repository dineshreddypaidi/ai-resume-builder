from dotenv import load_dotenv
import os

load_dotenv()



# project secrets loading form  .env

DEBUG = os.getenv('DEBUG', 'False')

SECRET_KEY = os.getenv('SECRET_KEY',"")

