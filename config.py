import os
from dotenv import load_dotenv

load_dotenv() # This is reading your envrionment variable file

DATABASES = {
    'ENGINE':'psycopg2',
    'HOST':os.getenv('DATABASE_HOST'),
    'USER':os.getenv('DATABASE_USER'),
    'PASSWORD':os.getenv('DATABASE_PSW'),
    'DBNAME':os.getenv('DATABASE_NAME'),
    'PORT': 5432
}


MS_ACCESS_KEY = os.getenv('MS_ACCESS_KEY')