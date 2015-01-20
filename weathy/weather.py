from abc import ABCMeta


class WeatherInformation(object):
    def __init__(self, city, country, lat, lon, temp, desc):
        self.city = city
        self.country = country
        self.latitude = lat
        self.longitude = lon
        self.temperature = temp
        self.description = desc


class Forecaster(object):
    __metaclass__ = ABCMeta

    def weather_info(self, lat, lon):
        pass