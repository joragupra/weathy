from weather import Forecaster, WeatherInformation
import json
import urllib


class OpenWeatherForecaster(Forecaster):
    def weather_info(self, latitude, longitude):
        data = json.loads(urllib.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?lat=' + str(latitude) + '&lon=' + str(
                longitude) + '&APPID=927392f02a87dd6a85c7a55a69ec3b9c&units=metric').read())
        return WeatherInformation(data['name'], data['sys']['country'], str(latitude), str(longitude),
                                  data['main']['temp'], data['weather'][0]['description'])