from flask import Flask, redirect, request, render_template
from contacts import Contact


app = Flask(__name__)


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
    return render_template("./test.html", contacts = contacts_set)
