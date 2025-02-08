from database.crud_operations import add_ngo, get_all_ngos

def register_ngo():
    name = input("Enter NGO Name: ")
    mission = input("Enter Mission: ")
    contact = input("Enter Contact Info: ")
    add_ngo(name, mission, contact)

def list_ngos():
    ngos = get_all_ngos()
    for ngo in ngos:
        print(f"{ngo['name']} - {ngo['mission']} - {ngo['contact']}")
