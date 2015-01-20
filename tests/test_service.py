import unittest
import weathy.net
import weathy.geo
import weathy.weather
from weathy.service import PromptWeather, PromptInformation

test_ip_address = "199.000.111.222"
test_city = "Farmville"
test_country = "Wonderland"
test_latitude = 100.0
test_longitude = 200.0
test_temperature = 20
test_conditions = "mostly cloudy"


class NetLocatorStub(weathy.net.IpAddressLocator):
    def ip_address_for_local_machine(self):
        return weathy.net.IpAddress(test_ip_address)


class GeoLocatorStub(weathy.geo.GeoLocator):
    def geo_location(self, ip_address):
        if ip_address == test_ip_address:
            return weathy.geo.GeoLocation(city=test_city, country=test_country, lat=test_latitude,
                                                  lon=test_longitude)
        return None


class ForecasterStub(weathy.weather.Forecaster):
    def weather_info(self, lat, lon):
        if lat == test_latitude and lon == test_longitude:
            return weathy.weather.WeatherInformation(country=test_country, city=test_city, lat=test_latitude,
                                                             lon=test_longitude, temp=test_temperature,
                                                             desc=test_conditions)
        return None


class PromptWeatherTest(unittest.TestCase):
    def setUp(self):
        self.weathy = PromptWeather(net_locator=NetLocatorStub(), geo_locator=GeoLocatorStub(),
                                            weather_forecaster=ForecasterStub())

    def test_retrieve_weather(self):
        weather_info = self.weathy.retrieve_weather()
        self.assertEqual(test_city, weather_info.city)
        self.assertEqual(test_conditions, weather_info.conditions)
        self.assertEqual(test_temperature, weather_info.temperature)


if __name__ == '__main__':
    unittest.main()