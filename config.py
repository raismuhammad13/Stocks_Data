import os
from dotenv import load_dotenv

load_dotenv() # This is reading your envrionment variable file

DATABASES = {
    'HOST':os.getenv('DATABASE_HOST')
}