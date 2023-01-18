from sqlite3 import connect
import psycopg2


def insert_sale(connection, order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount):
    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount
    sale_data = (order_num, order_type, cust_name, prod_number,
                 prod_name, quantity, price, discount, order_total)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO sale (ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', sale_data)
    connection.commit()
    cursor.execute(
        'SELECT CUST_NUM, ORDER_TOTAL FROM sale WHERE ORDER_NUM=%s', (order_num))
    rows = cursor.fetchall()
    for row in rows:
        print('Customer Name:', row[0])
        print('Total Order:', row[1])


if __name__ == '__maim__':
    connection = psycopg2.connect(database='company_sales', user='n_dasha',
                                  password='24465336Kotiki', host='localhost', port='5432')
    order_num = int(input(''))
    order_type = input('')
    custom_name = input('')
    prod_num = input('')
    prod_name = input('')
    quantity = float(input(''))
    price = float(input(''))
    discount = float(input(''))
    insert_sale(connection, order_num, order_type, custom_name,
                prod_num, prod_name, quantity, price, discount)
    connection.close()
