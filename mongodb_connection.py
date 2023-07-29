import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

mongodb_connection = f"mongodb://{user}:{password}@{host}:{port}/{db_name}"
client = MongoClient(host=mongodb_connection)
