from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database Banaye
conn = sqlite3.connect("bookings.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS bookings(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
mobile TEXT,
service TEXT
)
""")

conn.commit()
conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():

    name = request.form["name"]
    mobile = request.form["mobile"]
    service = request.form["service"]

    conn = sqlite3.connect("bookings.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO bookings(name,mobile,service) VALUES(?,?,?)",
        (name, mobile, service)
    )

    conn.commit()
    conn.close()

    return "<h1>Booking Success ✅</h1>"


@app.route("/admin")
def admin():

    conn = sqlite3.connect("bookings.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM bookings")
    data = cur.fetchall()

    conn.close()

    return str(data)


if __name__ == "__main__":
    app.run(debug=True)
