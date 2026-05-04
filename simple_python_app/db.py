import sqlite3

def setup_db(db_name):
    connector = sqlite3.connect(f"{db_name}.db")
    mydb = connector.cursor()
    mydb.execute(f"CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMARY KEY, first_name VARACHAR, last_name VARACHAR, middle_name VARACHAR, email VARACHAR);")