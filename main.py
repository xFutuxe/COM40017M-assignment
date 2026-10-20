def main_menu():
    print("Welcome to the Album Log Tracker!")
    print("Please choose an option:")
    print("1. Add a new album")
    print("2. View all albums")
    print("3. Search for an album")
    print("4. Exit")

    input_choice = input("Enter your choice (1-4): ").strip()
    if input_choice == "1":
        pass
    elif input_choice == "2":
        pass
    elif input_choice == "3":
        pass
    elif input_choice == "4":
        print("Exiting the Album Log Tracker. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu() 