import mysql.connector
from geopy import distance

def get_airport_by_icao(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        print(result[0])
        return result[0]

connection = mysql.connector.connect(
        host='localhost',
        port= 3306,
        database='flight_game',
        user='root',
        password='12345',
        autocommit=True
        )

icao1 = input('Enter the ICAO of the airport: ')
icao2 = input('Enter the ICAO of the airport: ')
lat_long1 = get_airport_by_icao(icao1)
lat_long2 = get_airport_by_icao(icao2)
print(f'Distance between the two airports:{distance.distance(lat_long1, lat_long2)}')