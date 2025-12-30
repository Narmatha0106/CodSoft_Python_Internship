contacts={}
def add_contact():
    name=input("Name:")
    phone=input("Phone:")
    email=input("Email:")
    address=input("Address:")
    contacts[name]={"Phone":phone,"Email":email,"Address":address}
    print("Contact added successfully!")
def view_contacts():
    for name,info in contacts.items():
        print(f"\nName:{name}")
        print("Phone:",info["Phone"])
        print("Email:",info["Email"])
        print("Address:",info["Address"])
def search_contact():
    name=input("Enter name to search:")
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")
def update_contact():
    name=input("Enter name to update:")
    if name in contacts:
        contacts[name]["Phone"]=input("New Phone:")
        contacts[name]["Email"]=input("New Email:")
        contacts[name]["Address"]=input("New Address:")
        print("Contact uploaded.")
    else:
        print("Contact not found.")
def delete_contact():
    name=input("enter name to delete:")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")
while True:
        
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    choice=input("Choose option:")
    if choice=="1":
        add_contact()
    elif choice=="2":
        view_contacts()
    elif choice=="3":
        search_contact()
    elif choice=="4":
        update_contact()
    elif choice=="5":
        delete_contact()
    elif choice=="6":
        break
    else:
        print("Invalid choice")
                   