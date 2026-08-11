import csv

class Contact:
    total_contacts = 0
    contact_list = []

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        Contact.contact_list.append(self)
        Contact.total_contacts+=1

    @classmethod
    def search(cls, query):
        return

    @classmethod
    def all(cls):
        return cls.contact_list

def initialize_contacts():
    with open("contacts.txt", newline="") as file_data:
        contact_rows= csv.reader(file_data, delimiter=",")
        for row in contact_rows:
            Contact(row[0], row[1], row[2])
        



