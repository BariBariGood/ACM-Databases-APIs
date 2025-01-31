# MongoDB Atlas Setup Guide

This guide will walk you through setting up **MongoDB Atlas** from a fresh account and preparing it for use in your Python application.

---

## **Step 1: Create a MongoDB Atlas Account**
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register).
2. Sign up for an account or log in if you already have one.
3. Click **"Create a New Project"** and give it a name (e.g., `MyMongoProject`).
4. Click **"Next"** and then **"Create a Cluster"**.

---

## **Step 2: Deploy a Free Cluster**
5. Choose the **M0 (Free Tier)** cluster size.
6. Name your cluster (e.g., `acm-demo-test1`).
7. Click **"Create Deployment"**.

---

## **Step 3: Set Up Database Access (User & Password)**
2. Click **"Create Database User"**.
3. **Username:** Choose a username
4. **Password:** Choose a strong password.
6. Click **"Add User"**.
Move on via "Choose a connection method"

---

## **Step 4: Connect to Your Cluster**
3. Choose **"Drivers"**.
4. Select **Python** as the driver and version `4.7 or later`.
5. copy paste connection string at the bottom into the .env file
5. Click done

## **Step 5: Set Up Network Access (IP Whitelist)**
1. Go to **"Network Access"** on the left sidebar.
2. Click **"Add IP Address"**.
3. Choose **"Allow Access from Anywhere"** (`0.0.0.0/0`) (Recommended for testing).
4. Click **"Confirm"**.

---



   ```
   mongodb+srv://<username>:<password>@acm-demo-test1.pabqm.mongodb.net/?retryWrites=true&w=majority
   ```
6. Replace `<username>` and `<password>` with your database credentials.

---

## **Step 6: Prepare Your Python Project**
1. Create a `.env` file in your project directory:
   ```bash
   touch .env
   ```
2. Paste the connection string inside `.env`:
   ```
   MONGO_URI=mongodb+srv://<username>:<password>@acm-demo-test1.pabqm.mongodb.net/?retryWrites=true&w=majority
   ```
3. Ensure `.env` is ignored by adding it to `.gitignore`:
   ```
   echo ".env" >> .gitignore
   ```

---

## **Step 7: Verify Connection in Python**
Create a Python script `test_connection.py`:

```python
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
```

Run the script:
```bash
python test_connection.py
```

Expected output:
```
Pinged your deployment. You successfully connected to MongoDB!
```

---

## **Step 8: Create a Database and Collection**
1. Go to your **MongoDB Atlas Cluster**.
2. Click **"Browse Collections"**.
3. Click **"Add My Own Data"**.
4. Enter `cs_club_demo` as the database name.
5. Enter `students` as the collection name.
6. Click **"Create"**.

Your database is now set up and ready for use in your Python application!

---

## **Next Steps**
✅ **Set up a MongoDB Atlas cluster**
✅ **Configured access and security**
✅ **Connected to MongoDB Atlas from Python**
✅ **Created a database and collection**

Now you can proceed with inserting and retrieving data as shown in the main tutorial.

---