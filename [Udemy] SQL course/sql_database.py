# Python Database API Specification

import sqlite3
with sqlite3.connect('movie_library.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Movies (
        Title TEXT,
        Director TEXT,
        Year INT
    )
    ''')

    # cursor.execute(
    #     "INSERT INTO Movies VALUES ('Avatar', 'James Cameron', 2009)")
    # feching records
    # cursor.execute("SELECT * FROM Movies")
    # print(cursor.fetchone())

    # adding more records
    # high_earning_movies = [
    #     ("Avengers:Endgame", "Russo Brothers", 2019),
    #     ("Star Wars: The Force Awaken", "J.J. ABrams", 2015)
    # ]

    # cursor.executemany("INSERT INTO Movies Values (?,?,?)",
    #                    high_earning_movies)
    # records = cursor.execute("SELECT * FROM Movies")
    # print(cursor.fetchall())

    # Filter records
    release_year = (2015,)
    cursor.execute("SELECT * FROM Movies WHERE Year >=?", release_year)
    print(cursor.fetchall())
    connection.commit()
