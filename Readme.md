# MongoDB Atlas Python Integration

This guide provides step-by-step instructions to set up and interact with **MongoDB Atlas** using **Python**, starting from setting up a virtual environment to performing CRUD operations.

---

## **Step 1: Project Setup**

### **1.1 Create a Project Directory**
```bash
mkdir mongodb-demo
cd mongodb-demo
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

Install the necessary MongoDB Python driver:

```bash
pip install "pymongo[srv]"
```

Verify installation:

```bash
pip freeze | grep pymongo
```

---

## **Step 3: Prepare JSON Data**

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

## **Step 4: Python Script to Work with MongoDB**

Create a new Python file called `mongodb_app.py`:

```python
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Atlas connection string (replace with your credentials)
uri = "mongodb+srv://indelrio:0310@acm-demo-test1.pabqm.mongodb.net/?retryWrites=true&w=majority"

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

# Insert data into MongoDB
insert_result = collection.insert_many(students_data)
print(f"Inserted {len(insert_result.inserted_ids)} documents into the students collection.")

# Retrieve and display all documents
print("\nRetrieved documents from MongoDB:")
for student in collection.find():
    print(student)

# Optional: Cleanup - Comment to keep data
# collection.delete_many({})
# print("\nDeleted all records after demonstration.")

client.close()
```

---

## **Step 5: Running the Script**

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

## **Step 6: Verify Data in MongoDB Atlas**

1. Go to **MongoDB Atlas Dashboard.**
2. Navigate to your cluster and click **"Browse Collections."**
3. Select the **`cs_club_demo.students`** collection to view the inserted data.
4. Click **Refresh** if needed.

---

## **Step 7: Additional Operations**

### **7.1 Query Data Using Filters**

```python
print("\nStudents older than 21:")
for student in collection.find({"age": {"$gt": 21}}):
    print(student)
```

### **7.2 Update a Document**

```python
collection.update_one({"name": "Alice Johnson"}, {"$set": {"age": 22}})
print("\nUpdated Alice's age to 22.")
```

### **7.3 Delete a Document**

```python
collection.delete_one({"name": "Bob Smith"})
print("\nDeleted Bob Smith's record.")
```

### **7.4 Delete All Data (Cleanup)**

```python
collection.delete_many({})
print("Deleted all student records.")
```

---

## **Step 8: Deactivate Virtual Environment**

When done, deactivate the virtual environment:

```bash
deactivate
```

---

## **Step 9: Troubleshooting**

1. **No data showing in Atlas?**
   - Ensure you're viewing the correct database and collection.
   - Refresh the collection page.

2. **Connection issues?**
   - Verify that your IP is whitelisted in Atlas under **"Network Access."**
   - Double-check username/password in the connection string.

3. **Module not found?**
   - Ensure `pymongo` is installed in the correct environment using:
     ```bash
     pip list | grep pymongo
     ```

---

## **Step 10: Summary of Steps**

1. **Set up virtual environment:** `python3 -m venv venv && source venv/bin/activate`
2. **Install dependencies:** `pip install "pymongo[srv]"`
3. **Prepare JSON file with data.**
4. **Write Python script to insert and retrieve data.**
5. **Run the script and verify results in Atlas.**
6. **Perform additional queries, updates, and deletions.**
7. **Deactivate the environment when done.**

---

