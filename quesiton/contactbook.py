contactBook = {}

while True:
    print("\nWhat Task You Want to Perform? Please choose (1/5)")
    print("1. Add a Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = int(input("Enter: "))

    if choice == 1:
        print("\nYou Chose Option 1")
        key = input("Enter name: ")
        value = int(input("Enter mobile no: "))
        contactBook[key] = value
        print("Contact added successfully!")

    elif choice == 2:
        print("\nYou Chose Option 2")
        user_input = input("Enter the name or number to search: ")

        found = False
        for name, number in contactBook.items():
            if user_input == name or user_input == str(number):
                print(f"Contact Found: {name} → {number}")
                found = True
                break

        if not found:
            print("Contact Not Found!")

    elif choice == 3:
        print("\nYou Chose Option 3")
        delete = input("Enter the name you want to delete: ")

        if delete in contactBook:
            del contactBook[delete]
            print("Contact deleted successfully!")
        else:
            print("Error: Contact not found!")

    elif choice == 4:
        print("\nYou Chose Option 4")
        if contactBook:
            print("\nYour Contacts:")
            for name, number in contactBook.items():
                print(f"{name}: {number}")
        else:
            print("Contact book is empty!")

    elif choice == 5:
        print("\nExit successfully")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")
