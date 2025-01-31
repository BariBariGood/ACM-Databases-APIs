# MongoDB Atlas Python Integration

This guide provides step-by-step instructions to set up and interact with **MongoDB Atlas** using **Python**, starting from setting up a virtual environment to performing CRUD operations.

These instructions are intended for those setting up their own project. If you are cloning a repository, refer to the repository-specific instructions in the `README.md` file.

---

## **Step 1: Project Setup**

### **1.1 Open Project Directory**
```bash
ls
cd acm-mongo-fire
```

### **1.2 Set Up a Virtual Environment**

- **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

You should see `(venv)` at the beginning of your terminal prompt.

---

## **Step 2: Install Dependencies**

If you are setting up the project for the first time, install the necessary dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## **Step 3: Set Up Environment Variables**

Create a `.env` file in the project directory to store sensitive information:

```bash
touch .env
```

Add the following content to your `.env` file:

```
# MongoDB Atlas Connection String
# Replace <username>, <password>, and <cluster-url> with your actual MongoDB credentials
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority
```

---

## **Step 4: Prepare JSON Data**

Create a `data.json` file in the project directory:

```json
[
    {
        "name": "Alice Johnson",
        "age": 21,
        "major": "Computer Science"
    },
    {
        "name": "Bob Smith",
        "age": 23,
        "major": "Mathematics"
    },
    {
        "name": "Charlie Brown",
        "age": 22,
        "major": "Physics"
    }
]
```

---

## **Step 5: Python Script to Work with MongoDB**

Create a new Python file called `mongodb_app.py`:

```python
import json
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variables
uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
    exit(1)

# Select database and collection
db = client["cs_club_demo"]
collection = db["students"]

# Load data from JSON file
with open("data.json", "r") as file:
    students_data = json.load(file)

# Insert data into MongoDB collection
insert_result = collection.insert_many(students_data)
print(f"Inserted {len(insert_result.inserted_ids)} documents into the students collection.")

# Retrieve and display all documents
print("\nRetrieved documents from MongoDB:")
for student in collection.find():
    print(student)

client.close()
```

---

## **Step 6: Running the Script**

Run the Python script to insert and retrieve data:

```bash
python mongodb_app.py
```

**Expected Output:**
```
Pinged your deployment. You successfully connected to MongoDB!
Inserted 3 documents into the students collection.

Retrieved documents from MongoDB:
{'_id': ObjectId('...'), 'name': 'Alice Johnson', 'age': 21, 'major': 'Computer Science'}
{'_id': ObjectId('...'), 'name': 'Bob Smith', 'age': 23, 'major': 'Mathematics'}
{'_id': ObjectId('...'), 'name': 'Charlie Brown', 'age': 22, 'major': 'Physics'}
```

---

## **Step 7: Verify Data in MongoDB Atlas**

1. Go to **MongoDB Atlas Dashboard.**
2. Navigate to your cluster and click **"Browse Collections."**
3. Select the **`cs_club_demo.students`** collection to view the inserted data.
4. Click **Refresh** if needed.

---

## **Step 8: Deactivate Virtual Environment**

When done, deactivate the virtual environment:

```bash
deactivate
```

---

