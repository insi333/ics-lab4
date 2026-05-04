from flask import Flask, jsonify
import os
import sqlite3

from db import setup_db

group_name = os.getenv("DATABASE_NAME", 'KB_3')
setup_db(group_name)
app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name):
    return jsonify({"message": f"Hello {name}"})

@app.route('/students', methods=['GET'])
def all_students():
    connector = get_db_connector(group_name)
    mycursor = connector.cursor()
    mycursor.execute("SELECT * FROM Students")
    myresult = mycursor.fetchall()
    all_students = {}
    for i in myresult:
        student = {"first_name": i[1], "middle_name": i[2], "second_name": i[3], "email": i[4]}
        all_students[i[0]] = student
    return jsonify(all_students)

@app.route('/students/<id>', methods=['GET'])
def student_by_id(id):
    connector = get_db_connector(group_name)
    mycursor = connector.cursor()
    mycursor.execute(f"SELECT * FROM Students WHERE id = {id}")
    myresult = mycursor.fetchone()
    return jsonify(
        {"first_name": myresult[1],
         "middle_name": myresult[2], 
         "second_name": myresult[3], 
         "email": myresult[4]}) if myresult else jsonify({})

def get_db_connector(db_name):
    return sqlite3.connect(f"{db_name}.db")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)