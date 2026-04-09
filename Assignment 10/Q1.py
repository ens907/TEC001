import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
jokes_data = response.json()

print(jokes_data["value"])