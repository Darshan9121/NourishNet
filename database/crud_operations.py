from config.config import donors_collection, ngos_collection, volunteers_collection
from database.models import donor_schema, ngo_schema, volunteer_schema

# Insert a new donor
def add_donor(name, email, phone, location):
    donor = donor_schema(name, email, phone, location)
    donors_collection.insert_one(donor)
    print(f"✅ Donor {name} added successfully!")

# Retrieve all donors
def get_all_donors():
    return list(donors_collection.find({}, {"_id": 0}))

# Insert NGO
def add_ngo(name, mission, contact):
    ngo = ngo_schema(name, mission, contact)
    ngos_collection.insert_one(ngo)
    print(f"✅ NGO {name} added successfully!")

# Retrieve all NGOs
def get_all_ngos():
    return list(ngos_collection.find({}, {"_id": 0}))

# Insert Volunteer
def add_volunteer(name, skills, availability):
    volunteer = volunteer_schema(name, skills, availability)
    volunteers_collection.insert_one(volunteer)
    print(f"✅ Volunteer {name} added successfully!")

# Retrieve all volunteers
def get_all_volunteers():
    return list(volunteers_collection.find({}, {"_id": 0}))
