from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER", "admin")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME", "studentdb")


def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=3306
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    phone = request.form["phone"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO students (name, email, course, phone)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, email, course, phone))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("students"))


@app.route("/students")
def students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students ORDER BY id DESC")
    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("students.html", students=records)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)