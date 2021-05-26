from flask import Flask

app = Flask(__name__)

from app import routes

from flask_pymongo import PyMongo
 
app.config["MONGO_URI"] = "mongodb://localhost:27017/supsl"
mongo = PyMongo(app)

from pymongo import MongoClient

# Create the client
pmclient = MongoClient('localhost', 27017)

# Connect to our database
pmdb = pmclient.supsl

# Fetch our series collection
pmcollection = db.ddt
