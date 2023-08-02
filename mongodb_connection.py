import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

host = os.getenv("MONGODB_HOST")
port = os.getenv("MONGODB_PORT")
user = os.getenv("MONGODB_USER")
password = os.getenv("MONGODB_PASS")
db_name = os.getenv("MONGODB_NAME")

mongodb_connection = f"mongodb://{user}:{password}@{host}:{port}"
client = MongoClient(host=mongodb_connection)
