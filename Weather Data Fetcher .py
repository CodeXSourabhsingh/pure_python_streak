import requests  
from config import WEATHER_API_KEY

class WeatherApps:
   def __init__(self):
      self.API = WEATHER_API_KEY
      self.base_url = "http://api.openweathermap.org/data/2.5/weather"
   def get_weather(self,city):  
           url = f"{self.base_url}?q={city}&appid={self.API}&units=metric"

           try:
                response = requests.get(url)
                if response.status_code == 200:
                     data = response.json()
                     city_name = data["name"]
                     temp = data['main']['temp']
                     humidity = data['main']['humidity']
                     description = data['weather'][0]['description']
                     wind_speed = data['wind']['speed']

                     print(f"\n--- Weather in {city_name} ---")
                     print(f"Temperature: {temp}°C")
                     print(f"Humidity: {humidity}%")
                     print(f"Condition: {description.capitalize()}")
                     print(f"Wind Speed: {wind_speed} m/s\n") 

                elif response.status_code == 404:
                     print('city not found. please check the spelling')     
                elif response.status_code == 401:
                    print('invalid API key. check your config.py files ')
                    print(f"API error: {response.status_code}")
                else:
                     print(f"API error: {response.status_code}")    

           except requests.exceptions.RequestException as e:
                      
                      print(f"Network error: {e}")

   def run(self):
        print("Weather Data Fetcher ")
        while True:
            city = input("Enter city name (or 'exit' to quit): ").strip()
            if city.lower() == "exit":
                print("Goodbye!")
                break
            elif city == "":
                print("Please enter a city name.")
                continue
            else:
                self.get_weather(city)   


if __name__== "__main__":
    app = WeatherApps()
    app.run()
    



   


 

