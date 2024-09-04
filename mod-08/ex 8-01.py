import mysql.connector

def get_airport_by_icao(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        for row in result:
            print(f'{row[0]}, {row[1]}')
    return

connection = mysql.connector.connect(
        host='localhost',
        port= 3306,
        database='flight_game',
        user='root',
        password='12345',
        autocommit=True
        )

icao = input('Enter the ICAO of the airport: ')
get_airport_by_icao(icao)