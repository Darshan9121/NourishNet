import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Get database configuration
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Ensure all required configurations are present
if not MONGO_URI or not DATABASE_NAME:
    raise ValueError("❌ Missing database configuration in .env file!")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# Collections
donors_collection = db["donors"]
ngos_collection = db["ngos"]
volunteers_collection = db["volunteers"]

print("✅ Database connected successfully!")
