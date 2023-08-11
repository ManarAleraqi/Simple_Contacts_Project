import json

class Contacts:
    
    def init(self, name, phone_num, email):
        self.name = name
        self.phone_num = phone_num
        self.email = email
    
    @staticmethod
    def add():
        name = input("Name: ")
        phone_num = input("Phone Number: ")
        email = input("Email: ")
        contact = {
            'name': name,
            'phone_num': phone_num,
            'email': email
        }
        
        with open('contact.json', 'a') as file:
            json.dump(contact, file)
            file.write('\n')
        
        print("Contact added successfully!")
    
    @staticmethod
    def edit():
        name = input("Enter the name of the contact to edit: ")
        
        with open('contact.json', 'r+') as file:
            contacts = [json.loads(line) for line in file]
            
            for contact in contacts:
                if contact['name'] == name:
                    contact['phone_num'] = input("New phone number: ")
                    contact['email'] = input("New email: ")
            
            file.seek(0)
            file.truncate()
            
            for contact in contacts:
                json.dump(contact, file)
                file.write('\n')
        
        print("Contact edited successfully!")
    
    @staticmethod
    def delete():
        name = input("Enter the name of the contact to delete: ")
        
        with open('contact.json', 'r+') as file:
            contacts = [json.loads(line) for line in file]
            contacts = [c for c in contacts if c['name'] != name]
            
            file.seek(0)
            file.truncate()
            
            for contact in contacts:
                json.dump(contact, file)
                file.write('\n')
        
        print("Contact deleted successfully!")
    
    @staticmethod
    def show():
        with open('contact.json', 'r') as file:
            contacts = [json.loads(line) for line in file]
            for contact in contacts:
                print(contact)
    
print("1-Add contact\n2-Edit contact\n3-Delete contact\n4-Show my list")
num = input("Enter the number of the operation you want: ")

if num == '1':
    Contacts.add()
elif num == '2':
    Contacts.edit()
elif num == '3':
    Contacts.delete()
elif num == '4':
    Contacts.show()
else:
    print("Invalid input")