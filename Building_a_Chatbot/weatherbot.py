# Import necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests

# Initialize ChatBot with its storage adapter and name
chatbot = ChatBot('WeatherBot')

# Create a list of greeting and farewell conversations for training
conversation = [
    "Hi",
    "Hello!",
    "Hello",
    "Hi there!",
    "What's up?",
    "Not much, how can I assist you?",
    "How are you?",
    "I'm doing great, how can I assist you?",
    "Bye",
    "Bye!"
    "Goodbye",
    "Bye! Have a great day!",
    "I'm done",
    "It was nice talking to you. Goodbye!",
]

# Train the chatbot with the conversation list
trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Function to get weather information using OpenWeatherMap API
def get_weather(location):
    api_key = "c2bbb034e62c931609aaee8b5f042c86"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    try:
        city_name, state_code = location.split(", ")
        query = f"{city_name},{state_code},US"
    except ValueError:
        query = f"{location},US"
    complete_url = base_url + "appid=" + api_key + "&q=" + query + "&units=imperial"
    response = requests.get(complete_url)
    weather_data = response.json()
    if weather_data['cod'] == 200:
        main = weather_data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_description = weather_data['weather'][0]['description']
        return (f"Temperature: {temperature}°F\n"
                f"Humidity: {humidity}%\n"
                f"Description: {weather_description.capitalize()}")
    else:
        return "Sorry, I couldn't find the weather for that location."


# Introduce the chatbot and its capabilities
print("Hi! My name is WeatherBot, but I go by 🌤🤖. I can assist you with basic greetings, answer how I'm doing, say goodbye, and provide current weather information for any city in the US. To get a weather report, just type 'Weather: [city name], [state code]. For cities with unique names, simply typing 'Weather: [city name]' works too!")

# Main loop to handle chat input/output
while True:
    user_input = input("> ")
    if user_input.lower() in ["bye", "goodbye", "i'm done"]:
        print("🌤🤖: Goodbye! Have a great day!")
        break
    elif user_input.lower().startswith("weather: "):
        city = user_input.split(" ", 1)[1]
        weather_info = get_weather(city)
        print("🌤🤖:", weather_info)
    else:
        response = chatbot.get_response(user_input)
        print("🌤🤖:", response)