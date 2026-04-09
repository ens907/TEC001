from flask import Flask
app = Flask(__name__)

def check_if_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/prime_number/<int:number>")
def prime_number(number):
    status = check_if_prime(number)

    response = {
        "Number": number, 
        "isPrime": status
    }
    return response

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=5000)