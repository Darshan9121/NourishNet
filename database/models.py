from datetime import datetime

def donor_schema(name, email, phone, location):
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "location": location,
        "registered_at": datetime.utcnow()
    }

def ngo_schema(name, mission, contact):
    return {
        "name": name,
        "mission": mission,
        "contact": contact,
        "registered_at": datetime.utcnow()
    }

def volunteer_schema(name, skills, availability):
    return {
        "name": name,
        "skills": skills,
        "availability": availability,
        "joined_at": datetime.utcnow()
    }
