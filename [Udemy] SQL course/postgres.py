import psycopg2
connection = psycopg2.connect(
    database='company_sales',
    user='n_dasha',
    password='24465336Kotiki',
    host='localhost',
    port='5432'
)
cursor = connection.cursor()
cursor.execute('''CREATE TABLE sale 
(ORDER_NUM INT PRIMARY KEY, ORDER_TYPE TEXT, CUST_NAME TEXT, PROD_NUMBER TEXT, PROD_NAME TEXT, QUANTITY INT, PRICE REAL, DISCOUNT REAL, ORDER_TOTAL REAL)''')
connection.commit()
connection.close()
