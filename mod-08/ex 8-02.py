import mysql.connector

def get_airports_from_area(area_code):
    sql = f"SELECT name FROM airport WHERE iso_country = '{area_code}' ORDER BY type"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        for row in result:
            print(f'{row[0]}')
    return

connection = mysql.connector.connect(
        host='localhost',
        port= 3306,
        database='flight_game',
        user='root',
        password='12345',
        autocommit=True
        )

area_code = input('Enter the area code: ')
get_airports_from_area(area_code)