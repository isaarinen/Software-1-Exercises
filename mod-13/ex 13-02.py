from flask import Flask, request
import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        port= 3306,
        database='flight_game',
        user='root',
        password='12345',
        autocommit=True
        )

app = Flask(__name__)
@app.route('/airport/<ICAO>')
def GetAirportData(ICAO):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        for row in result:
            name = row[0]
            location = row[1]
    response = {
        "ICAO" : ICAO,
        "Name" : name,
        "Location" : location
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port=5000)