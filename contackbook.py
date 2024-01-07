class Contact:
    def __init__(self,name,phone_number,email,address):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.address=address

class ContactManager:
    def __init__(self):
        self.contacts=[]

    def add_contact(self,contact):
        self.contacts.append(contact)

    def view_details(self):
        for i,contact in enumerate(self.contacts,1):
           print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contacts(self,search_terms):
        for contact in self.contacts:
            if search_terms.lower() in contact.name.lower() or search_terms in contact.phone_number:
                print(f"Name: {contact.name}\n Phone Number: {contact.phone_number}\n Email: {contact.email}\n Address: {contact.address}\n")

    def update_contact(self,index,updated_contact):
        self.contacts[index]= updated_contact

    def delete_contact(self,index):
        del self.contacts[index]

def display_main_menu():
    print("----------Menu----------")
    print("1. Add contact ")
    print("2. View contact list ")
    print("3. Search contact ")
    print("4. Update contact ")
    print("5. Delete contact ")
    print("6. Exit. ")

def get_contact_details():
    name = input("Enter Name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    return Contact(name,phone_number,email,address)

def main():
    contact_manager = ContactManager()

    while True:
        print("\n")
        display_main_menu()

        choice = int(input("Enter your choice (1 to 6): "))

        if choice==1:
            contact=get_contact_details()
            contact_manager.add_contact(contact)
            print("Contact Added Successfully.")
        
        elif choice==2:
            contact_manager.view_details()

        elif choice==3:
            search_terms = input("Enter the name or phone number to search: ")
            contact_manager.search_contacts(search_terms)

        elif choice==4:
            index = int(input("Enter the index of contact to update: "))
            updated_contact = get_contact_details()
            contact_manager.update_contact(index,updated_contact)
            print("Contact updated successfully.")

        elif choice==5:
            index = int(input("Enter the index of contact to delete: "))
            contact_manager.delete_contact(index)
            print("Contact deleted successfully.")

        elif choice==6:
            print("Exiting programme.")
            break

        else:
            print("Invalid choice. Enter a valid choice between 1 and 6 .")

if __name__=="__main__":
    main()
    

