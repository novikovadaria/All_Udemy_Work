import sqlite3
with sqlite3.connect('students_info.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        Student ID INT,
        First Name TEXT,
        Last Name TEXT,
        Email Address TEXT
    )
    ''')
    cursor.execute(
        "INSERT INTO Student VALUES ('12', 'James','Cameron', 'cameron@email.com')")
    cursor.execute("SELECT Email Address FROM Student")
    print(cursor.fetchone())
    connection.commit()
