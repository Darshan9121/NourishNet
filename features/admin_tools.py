from database.crud_operations import get_all_donors, get_all_ngos, get_all_volunteers
from config.logger import log_info

def list_all_donors():
    donors = get_all_donors()
    if not donors:
        print("No donors found.")
    else:
        for donor in donors:
            print(f"{donor['name']} - {donor['email']} - {donor['phone']} - {donor['location']}")

def list_all_ngos():
    ngos = get_all_ngos()
    if not ngos:
        print("No NGOs found.")
    else:
        for ngo in ngos:
            print(f"{ngo['name']} - {ngo['mission']} - {ngo['contact']}")

def list_all_volunteers():
    volunteers = get_all_volunteers()
    if not volunteers:
        print("No volunteers found.")
    else:
        for volunteer in volunteers:
            print(f"{volunteer['name']} - Skills: {volunteer['skills']} - Availability: {volunteer['availability']}")

def admin_menu():
    while True:
        print("\n=== Admin Panel ===")
        print("1. View All Donors")
        print("2. View All NGOs")
        print("3. View All Volunteers")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            list_all_donors()
        elif choice == "2":
            list_all_ngos()
        elif choice == "3":
            list_all_volunteers()
        elif choice == "0":
            print("Exiting Admin Panel... 👋")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    admin_menu()
