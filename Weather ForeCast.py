import requests

import requests

def get_current_weather(api_key, city_name):
    # Base URL for the OpenWeatherMap API
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # Construct the complete URL with parameters
    complete_url = f"{base_url}q={city_name}&appid={api_key}"

    # Send a GET request to the OpenWeatherMap API
    response = requests.get(complete_url)

    # Parse the JSON response
    data = response.json()

    # Check if the request was successful
    if data['cod'] == 200:
        # Extract and return relevant weather information
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return {
            'city': city_name,
            'weather_description': weather_description,
            'temperature': temperature,
            'humidity': humidity
        }
    else:
        return None

def main():
    # Your OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'

    # City name for which you want to retrieve weather data
    city_name = 'Toronto'

    # Get current weather data
    weather_data = get_current_weather(api_key, city_name)

    # Display weather information
    if weather_data:
        print(f"Weather in {weather_data['city']}: {weather_data['weather_description']}")
        print(f"Temperature: {weather_data['temperature']} K")
        print(f"Humidity: {weather_data['humidity']}%")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()

