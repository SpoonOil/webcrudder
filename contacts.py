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
        self.errors = {}
        # TODO: add validation


    def get_errors(self):
        errors = {}


        #firstName
        if self.first == None or len(self.first) == 0:
            errors["first"] = "First Name cannot be empty"

        if self.last== None or len(self.last) == 0:
            errors["last"] = "Last Name cannot be empty"

        if self.phone == None or len(self.phone) == 0:
            errors["phone"] = "Phone # cannot be empty"

        if self.email == None or len(self.email) == 0:
            errors["email"] = "Email cannot be empty"

        return errors

    def save(self):
        self.errors = self.get_errors()
        if len(self.errors) > 0:
            return False

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
