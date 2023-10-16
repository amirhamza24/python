contact = {}

def showFunction():
    print(contact.items())
    print("Name \t Contact")

    for key in contact:
        print("{} \t {}".format(key, contact.get(key)))

while True:
    choice = int(input("1. Add new contact: \n"
                   "2. Search the contact: \n"
                   "3. Display the contact: \n"
                   "4. Edit the contact: \n"
                   "5. Delete the contact: \n"
                   "6. Exit \n"
                   "Please choose number between[1-6] -  "))

    if choice == 1:
        name = input("Add your contact name: ")
        phone = input("Add your phone number: ")
        contact[name] = phone

    elif choice == 2:
        contactName = input("Search the contact: ")

        if contactName in contact:
            print(contactName, "Contact Number is: ", contact[contactName])
        else:
            print("Not found the contact")

    elif choice == 3:
        if not contact:
            print("Contact book is empty.")
        else:
            showFunction()

    elif choice == 4:
        editContact = input("Enter your contact name for edit: ")

        if editContact in contact:
            phone = input("Edit your number: ")
            contact[editContact] = phone
            print("Contact updated successfully.")
            showFunction()
        else:
            print("Name is not found.")

    elif choice == 5:
        deleteContact = input("Which contact do you want to delete? ")

        if deleteContact in contact:
            deleteConfirm = input("Are you sure to delete this contact? [y/n] ")

            if deleteConfirm == "y" or deleteConfirm == "Y":
                contact.pop(deleteContact)
            showFunction()
        else:
            print("The name is not found in the contact list.")

    else:
        break

