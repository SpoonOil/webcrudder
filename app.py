import secrets

from flask import Flask, flash, redirect, request, render_template
from contacts import Contact, initialize_contacts

initialize_contacts()


app = Flask(__name__)

app.secret_key = secrets.token_hex(32)

@app.route("/")
def index():
    return redirect("/contacts")

@app.route("/contacts")
def contactsPage():
    search = request.args.get("q")
    if search is not None:
        contacts_set = Contact.search(search)
    else:
        contacts_set = Contact.all()
    return render_template("./index.html", contacts = contacts_set)


@app.route('/contacts/new', methods = ["GET"])
def contacts_new_get():
    return render_template("new.html", contact = Contact())

@app.route('/contacts/new', methods = ["POST"])
def contacts_new():
    c = Contact(
        request.form['first_name'],
        request.form['last_name'],
        request.form['phone'],
        request.form['email'])

    if c.save():
        flash("Created New Contact")
        return redirect("/contacts")
    else:
        return render_template("new.html", contact = c)
