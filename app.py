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


@app.route("/", methods=["GET", "POST"])
def index():

    conn = sqlite3.connect("site.db")
    c = conn.cursor()
    selectStar = c.execute("SELECT * FROM contacts")
    allContacts = selectStar.fetchall()
    colHeaders = selectStar.description
    conn.close()

    if request.method == "POST":
        insertRecords(request.form["name"], request.form["number"])
        return redirect(url_for("index"))

    return render_template("index.html", contacts=allContacts, headers=colHeaders)


if __name__ == "__main__":
    app.run(debug=True)
