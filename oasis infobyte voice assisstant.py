import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import googlesearch
import requests

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    speak("Hello! How can I help you today?")

def get_weather(city_name, country_name,api_key):
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
            
            speak(f"The weather in {city_name} is {weather_description}.\nThe temperature is {temperature} degrees Celsius.\nHumidity is {humidity} percent.\nWind speed is {wind_speed} meters per second.")
        else:
            speak("Sorry, I couldn't retrieve the weather information for that location.")
    else:
        speak("Failed to fetch geolocation data.")

# Function to recognize user's voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration= 0.5)
        audio = recognizer.listen(source,timeout=10, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio,language='en-US')
        print("User:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you please repeat?")
        return listen()
    except sr.RequestError:
        speak("Sorry, I'm having trouble processing your request. Please try again later.")
        return None

# Function to perform actions based on user's voice commands
def process_command(command):
    if "hello" in command:
        speak("Hello there!")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak("Today's date is " + current_date)
    elif "weather" in command:
        speak("Which city would you like to know the weather for?")
        city_name = listen()
        speak("Can you please specify the country code For example, US for United States:?")
        country_name =listen()
        if city_name and country_name:
            get_weather(city_name, country_name,api_key)


    elif "search" in command:
        speak("What would you like me to search for?")
        query = listen()
        if query:
            search_results = googlesearch.search(query, num=1, stop=1, pause=2)
            if search_results:
                search_results = list(search_results)
                webbrowser.open(search_results[0])
            else:
                speak("Sorry, I couldn't find any relevant results for your query.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    greet()
    api_key = "076e49ea600c32e44942f874744c0d2f"
    while True:
        command = listen()
        if command:
            process_command(command)








            
