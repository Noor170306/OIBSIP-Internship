import requests

def get_weather(city_name, country_name, api_key):
    # Fetch geolocation data
    geolocation_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_name}&limit=1&appid={api_key}"
    geolocation_response = requests.get(geolocation_url)
    
    if geolocation_response.status_code == 200 and geolocation_response.json():
        geolocation_data = geolocation_response.json()[0]
        lat = geolocation_data["lat"]
        lon = geolocation_data["lon"]
        
        # Fetch weather data
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        weather_response = requests.get(weather_url)
        
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            temperature = weather_data["main"]["temp"]
            weather_description = weather_data["weather"][0]["description"]
            wind_speed = weather_data["wind"]["speed"]
            humidity = weather_data["main"]["humidity"]
            date_time = weather_data["dt"]
            
            print(f"The weather in {city_name} is {weather_description}.\nThe temperature is {temperature} degrees Celsius.\nHumidity is {humidity} percent.\nWind speed is {wind_speed} meters per second.")
        else:
            print("Sorry, I couldn't retrieve the weather information for that location.")
    else:
        print("Failed to fetch geolocation data.")

if __name__=="__main__":
    city_name = input("Enter the city name: ")
    country_name = input("Enter the country code (e.g., US for United States): ")
    api_key = "076e49ea600c32e44942f874744c0d2f"  
    get_weather(city_name, country_name, api_key)
