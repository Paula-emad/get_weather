
import tkinter as tk
import requests
import json
from datetime import datetime

# Function to get weather data
def get_weather():
    # Replace YOUR_API_KEY with your own OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    # Replace YOUR_CITY with your city name
    city = "YOUR_CITY"
    # API request URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # Send API request
    response = requests.get(url)
    # Parse response JSON
    data = json.loads(response.text)
    # Extract weather information
    weather = data["weather"][0]["description"].capitalize()
    temperature = int(data["main"]["temp"])
    # Return weather information
    return f"{temperature}°C, {weather}"

# Create GUI window
window = tk.Tk()
window.title("Clock & Weather")
window.geometry("300x150")

# Create label for displaying time
time_label = tk.Label(window, font=("Arial", 40))
time_label.pack(pady=10)

# Create label for displaying weather
weather_label = tk.Label(window, font=("Arial", 20))
weather_label.pack()

# Function to update time label
def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    # Schedule next update in 1 second
    time_label.after(1000, update_time)

# Function to update weather label
def update_weather():
    current_weather = get_weather()
    weather_label.config(text=current_weather)
    # Schedule next update in 10 minutes
    weather_label.after(600000, update_weather)

# Start updating time and weather labels
update_time()
update_weather()

# Start GUI loop
window.mainloop()
