import requests
import sys


api_key = "0933d47a01304ac2ed1f62bbfb74f637"


def main():
    if len(sys.argv) < 2:
        sys.exit("Please input the city!")
    city = " ".join(sys.argv[1:]).title()
    weather_info = get_weather(city)
    temperature_celcius, temperature_fahrenheit = get_temperature(weather_info)
    weather_type = get_weather_type(weather_info)
    print(
        f"Current temperature in {city} is {
            round(temperature_celcius)}°C ({round(temperature_fahrenheit)}°F). Current weather: {weather_type} ")


def get_weather(city):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    if response.status_code != 200:
        sys.exit("City was not found!")
    weather_info = response.json()
    return weather_info


def get_temperature(weather):
    temperature_kelvin = weather['main']['temp']
    return kelvin_to_celcius(temperature_kelvin), kelvin_to_fahrenheit(temperature_kelvin)


def kelvin_to_celcius(temperature):
    factor = 273.15
    return temperature - factor


def kelvin_to_fahrenheit(temperature):
    return kelvin_to_celcius(temperature) * 1.8 + 32


def get_weather_type(weather):
    return weather['weather'][0]['description']


if __name__ == "__main__":
    main()
