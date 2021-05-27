from flask import Flask
from flask import request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/supsl"
mongo = PyMongo(app)

#base = "http://127.0.0.1:5000"
#base = request.base_url


from app import routes
#from app import uproutes


if __name__ == "__main__":
    app.run(host='0.0.0.0')
 


#from pymongo import MongoClient

# Create the client
#pmclient = MongoClient('localhost', 27017)

# Connect to our database
#pmdb = pmclient.supsl

# Fetch our series collection
#pmcollection = db.ddt
