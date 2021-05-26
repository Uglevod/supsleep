from flask import Flask

app = Flask(__name__)

from app import routes

from pymongo import MongoClient

# Create the client
client = MongoClient('localhost', 27017)

# Connect to our database
db = client.supsl

# Fetch our series collection
collection = db.ddt
