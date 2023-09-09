from typing import Dict, List, Tuple, Union
import requests
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

api_key = os.getenv('api_key')



class WeatherAPI:
    def __init__(self, city: str):
        self.city = city

    def get_city_geo(self, api_key: str) -> Tuple[float, float]:
        """
        This function defines the city coordinates : latitude and longitude

        params: str
        output: float
        """
        coor_url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.city}&appid={api_key}"
        coordinates_response = requests.get(coor_url)
        coor_data = coordinates_response.json()
        lat = coor_data[0]["lat"]
        lon = coor_data[0]["lon"]
        return lat, lon

    def get_weather(self, api_key: str) -> Dict[str, Union[str, int, float]]:
        """
        This function makes a request for all available data for the current weather in the city

        params: str
        output: dict
        """
        lat, lon = self.get_city_geo(api_key)
        weather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=minutely,hourly,alerts,current&appid={api_key}"
        weather_response = requests.get(weather_url)
        city_data = weather_response.json()
        return city_data

    def show_weather(self, api_key: str) -> str:
        """
        This function defines values for temperature, humidity and wind speed and prints it out

        params: str
        output: str
        """
        city_data = self.get_weather(api_key)
        temp = city_data["daily"][0]["temp"]["day"]
        humidity = city_data["daily"][0]["humidity"]
        wind_speed = city_data["daily"][0]["wind_speed"]
        print(
            f"Temperature in {self.city}: {temp}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s"
        )


class WeatherForecast(WeatherAPI):
    def get_forecast(self, api_key: str) -> List[Dict[str, Union[str, int, float]]]:
        """
        This function defines values for temperature, humidity and wind speed for the next 5 days
        This function expands the get_weather function by fetching data for 5 days

        params: str
        output: list
        """
        weather_data = self.get_weather(api_key)
        forecast_data = []

        for day_data in weather_data["daily"][1:6]:
            temp = day_data["temp"]["day"]
            humidity = day_data["humidity"]
            wind_speed = day_data["wind_speed"]
            forecast_data.append(
                {"temp": temp, "humidity": humidity, "wind_speed": wind_speed}
            )

        return forecast_data


def main():
    city_name = "Odessa"
    odessa = WeatherAPI(city_name)
    odessa.show_weather(api_key)

    weather_forecast = WeatherForecast(city_name)
    forecast_data = weather_forecast.get_forecast(api_key)
    for i, day in enumerate(forecast_data, 1):
        temp = day["temp"]
        humidity = day["humidity"]
        wind_speed = day["wind_speed"]
        print(
            f"Day {i}: Temperature: {temp}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s"
        )


if __name__ == "__main__":
    main()
