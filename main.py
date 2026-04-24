# main.py

from file_handler import load_data
from profile import enter_profile, show_profile
from budget import show_budget

def main():
    print("====================")
    print("   Income Planner")
    print("====================")

    data = load_data()
    if data:
        print("Welcome back,", data["name"] + "!")

    while True:
        print("\n--- Menu ---")
        print("1. Enter / Update profile")
        if data:
            print("2. View budget split")
            print("3. View my profile")
        print("0. Exit")

        choice = input("\nYour choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            data = enter_profile()
        elif choice == "2" and data:
            show_budget(data)
        elif choice == "3" and data:
            show_profile(data)
        else:
            print("Invalid choice. Try again.")

main()
