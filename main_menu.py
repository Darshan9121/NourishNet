from features.donor_tools import register_donor, list_donors
from features.ngo_features import register_ngo, list_ngos
from features.volunteer_mgmt import register_volunteer, list_volunteers

def main_menu():
    while True:
        print("\n=== NourishNet Console App ===")
        print("1. Register Donor")
        print("2. View Donors")
        print("3. Register NGO")
        print("4. View NGOs")
        print("5. Register Volunteer")
        print("6. View Volunteers")
        print("0. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            register_donor()
        elif choice == "2":
            list_donors()
        elif choice == "3":
            register_ngo()
        elif choice == "4":
            list_ngos()
        elif choice == "5":
            register_volunteer()
        elif choice == "6":
            list_volunteers()
        elif choice == "0":
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
