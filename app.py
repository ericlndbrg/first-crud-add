from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)


def insertRecords(name, number):
    conn = sqlite3.connect("site.db")
    c = conn.cursor()
    c.execute("INSERT INTO contacts VALUES (:name, :phone_number)", {"name": name, "phone_number": number})
    conn.commit()
    conn.close()
    return None


def deleteRecords(name):
    conn = sqlite3.connect("site.db")
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE name=:name", {"name": name})
    conn.commit()
    conn.close()
    return None


@app.route("/", methods=["GET", "POST"])
def index():

    conn = sqlite3.connect("site.db")
    c = conn.cursor()
    selectStar = c.execute("SELECT * FROM contacts")
    allContacts = selectStar.fetchall()
    colHeaders = selectStar.description
    conn.close()

    if request.method == "POST":
        if "add-name" in request.form and "add-number" in request.form:
            insertRecords(request.form["add-name"], request.form["add-number"])
            return redirect(url_for("index"))
        elif "delete-name" in request.form:
            deleteRecords(request.form["delete-name"])
            return redirect(url_for("index"))

    return render_template("index.html", contacts=allContacts, headers=colHeaders)


if __name__ == "__main__":
    app.run(debug=True)
