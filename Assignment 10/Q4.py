import json
from flask import Flask

app = Flask(__name__)

with open("airports-1.json", "r") as file:
    airports_data = json.load(file)

@app.route("/airport/<icao>")
def get_airport(icao):

    icao = icao.upper()
    
    airport = airports_data.get(icao)

    if airport:
        return {
            "icao": airport["icao"],
            "name": airport["name"],
            "city": airport["city"],
            "country": airport["country"]
        }
    
    return {"message": "Not found"}, 404

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=5000)