import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    host = os.getenv('HOST')
    database = os.getenv('DATABASE')
    db_user = os.getenv('DB_USER')
    password = os.getenv('PASSWORD')