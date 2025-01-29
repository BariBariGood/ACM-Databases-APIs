from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection (replace with your credentials)
MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["cs_club_demo"]
collection = db["students"]

@app.route("/")
def home():
    return "Welcome to the Student Data API!"

@app.route("/students", methods=["GET"])
def get_students():
    students = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's default _id field
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)
