contacts = []
# add contact
def add_contact():
    name = input("Enter Name : ")
    phone = int(input("Enter Number : "))
    email = input("Enter Email(Optional) : ")

    contact = {
        "name" : name,
        "phone" : phone,
        "email" : email

    }
    contacts.append(contact)
    print("contact added in your device.")

# view contact 
def view_contact():
    if not contacts:
        print("no contact found!!!")
        return
    print("\n------ Contact List ------")
    for c in contacts:
        print(f"Found --> Name:{c['name']} , Phone:{c['phone']} , Email:{c['email']}")
    print()

# search contact 
def search_contact():  
    keyboard = input("Enter number or Name for search : ")

    Found = False
    for c in contacts:
        if keyboard.lower() in c['name'].lower() or keyboard in c['phone']:
            print(f"Found --> Name:{c['name']} , Phone:{c['phone']} , Email{c['email']}")
            print()
    if not Found:
        print("No matching contact found!\n")

# delete contact 
def delete_contact():
    name = input("Enter Name Which You Want to delete ")

    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("Contact Deleted!")
            return
    print("No contact found with this name!\n")

# update contact 
def update_contact():
    name = input("Enter name Which you want to update : ")

    for c in contacts:
        if c['name'].lower() == name.lower():
            print("Leave blank if you don't want to change.")
            
            new_phone = input("Enter Number")
            new_Email = input("Enter Email ")

            if new_phone:
                c['phone'] = new_phone
            if new_Email:
                c['email'] = new_Email

            print("Contact updated!\n")
            return
        print("No contact found!\n")


while True:
    print("""
-----book menu -----
    1. Add Contact
    2. View All Contacts
    3. Search Contact
    4. Delete Contact
    5. Update Contact
    6. Exit 
""")
    choice = input("choose 1-6 : ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid Number pls try again")




    