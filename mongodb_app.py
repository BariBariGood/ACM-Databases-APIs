import json
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB connection string (replace with your credentials)
uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
    exit(1)

# Select the database and collection
db = client["cs_club_demo"]
collection = db["students"]

# Load data from JSON file
with open("data.json", "r") as file:
    students_data = json.load(file)

# Insert data into MongoDB collection
result = collection.insert_many(students_data)
print(f"Inserted {len(result.inserted_ids)} documents into the students collection.")

# Retrieve and display data from MongoDB
print("\nRetrieved documents from MongoDB:")
for student in collection.find():
    print(student)

# # Optional: Cleanup - Delete all documents after the demo
# collection.delete_many({})
# print("\nDeleted all records after demonstration.")

# Close the MongoDB connection
client.close()
