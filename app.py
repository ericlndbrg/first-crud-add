from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect("site.db")
    cur = conn.cursor()
    getAllContacts = cur.execute("SELECT * FROM contacts")
    contacts = getAllContacts.fetchall()
    colHeaders = getAllContacts.description
    conn.close()
    return render_template("index.html", title="Home", contacts=contacts, colHeaders=colHeaders)


if __name__ == "__main__":
    app.run(debug=True)
