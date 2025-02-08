from database.crud_operations import add_donor, get_all_donors

def register_donor():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    location = input("Enter Location: ")
    add_donor(name, email, phone, location)

def list_donors():
    donors = get_all_donors()
    for donor in donors:
        print(f"{donor['name']} - {donor['email']} - {donor['phone']} - {donor['location']}")
