import requests

api_key = "2840c95fe26f5a1fefd37fae4eb2118f"
city = "Hanoi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

desc = data["weather"][0]["description"]
temp = data["main"]["temp"]

print(f"Weather: {desc}")
print(f"Temperature: {temp}°C")