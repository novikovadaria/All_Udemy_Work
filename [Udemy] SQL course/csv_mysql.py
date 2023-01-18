
import mysql.connector as mysql
import csv
connection = mysql.connect(
    user='root',
    password='24465336Kotiki',
    host='localhost',
    database='accs'
)

cursor = connection.cursor()
query = '''CREATE TABLE acc (
    id INT(255) NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    password_em VARCHAR(255) NOT NULL,
    vpn VARCHAR(255) NOT NULL,
    rulog VARCHAR(255) NOT NULL,
    rupass VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);'''
cursor.execute("DROP TABLE IF EXISTS acc")
cursor.execute(query)
with open("акки рулейт.xlsx", 'r', encoding='utf-8') as file:
    csv_data = csv.reader(file)
    for row in csv_data:
        print('row is a list', row)

        row_tuple = tuple(row)
        cursor.execute("""INSERT INTO acc (email, password_em,vpn, rulog,rupass)
        VALUES ("%s","%s","%s","%s","%s")
        """, row_tuple)
connection.commit()
cursor.execute("SELECT * FROM acc LIMIT 10 ")
print(cursor.fetchall())
connection.close()
