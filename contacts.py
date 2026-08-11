import csv

class Contact:
    total_contacts = 0
    contact_list = []

    def __init__(self, firstn = None, lastn = None, email = None, phone = None):
        self.id = Contact.total_contacts + 1,
        self.first = firstn
        self.last = lastn
        self.email = email
        self.phone = phone
        # TODO: add validation
        self.errors = {}

    def save(self):
        Contact.total_contacts+=1
        Contact.contact_list.append(self)
        return True


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
            c = Contact(row[0], row[1], row[2], row[3])
            c.save()
            
        



