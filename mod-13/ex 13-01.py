from flask import Flask, request

app = Flask(__name__)
@app.route('/prime_number/<number>')
def IsPrime(number):
    isPrime = False
    if 4 > int(number) > 0:
        isPrime = True
    elif int(number) < 1:
        isPrime = False
    else:
        isPrime = True
        for i in range(2, int(number)):
            if int(number) % i == 0:
                isPrime = False
    response = {
        "Number" : number,
        "IsPrime" : isPrime
    }        
    return response


if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port=5000)