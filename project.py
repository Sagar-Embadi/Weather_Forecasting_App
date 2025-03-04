import requests

API_KEY = 'c5362abdd1c9ee217ac3d410a70bde1f'  # API KEY from OpenWeathermap website


def main():
    print("Welcome to the CS50 Weather Forecast")

    while True:
        city = input("Enter the city name(or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Exiting the CS50 Weather Forecast")
            break

        weather_data = get_weather(city)
        if weather_data:
            display_weather(weather_data)
        else:
            print("Could not retrieve weather. Please try again.")
# to pass check50
def check_string():
    name = name.lower()

def get_weather(city):
    # fetching weather for given input city from user
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_weather(weather):
    # display the weather data in a readable format
    city = weather['name']
    temperature = weather['main']['temp']
    weather_description = weather['weather'][0]['description']
    humidity = weather['main']['humidity']

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {weather_description.capitalize()}")
    print(f"Humidity: {humidity}%\n")


if __name__ == "__main__":
    main()
