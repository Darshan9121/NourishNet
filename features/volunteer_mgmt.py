from database.crud_operations import add_volunteer, get_all_volunteers

def register_volunteer():
    name = input("Enter Name: ")
    skills = input("Enter Skills: ")
    availability = input("Enter Availability: ")
    add_volunteer(name, skills, availability)

def list_volunteers():
    volunteers = get_all_volunteers()
    for volunteer in volunteers:
        print(f"{volunteer['name']} - Skills: {volunteer['skills']} - Availability: {volunteer['availability']}")
