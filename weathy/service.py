import net_impl
import geo_impl
import weather_impl


class PromptInformation(object):
    def __init__(self, city, temp, conditions):
        self.city = city
        self.temperature = temp
        self.conditions = conditions


class PromptWeather(object):
    def __init__(self, net_locator=net_impl.JsonTestServiceIpAddressLocator(), geo_locator=geo_impl.IpApiGeoLocator(),
                 weather_forecaster=weather_impl.OpenWeatherForecaster()):
        """
        :param net_locator: net.IpAddressLocator
        :param geo_locator: geo.GeoLocator
        :param weather_forecaster: weather.Forecaster
        :return:
        """
        self.net_locator = net_locator
        self.geo_locator = geo_locator
        self.weather_forecaster = weather_forecaster

    def retrieve_weather(self):
        ip = self.net_locator.ip_address_for_local_machine()
        geo_data = self.geo_locator.geo_location(ip.ip_address)
        weather_data = self.weather_forecaster.weather_info(geo_data.latitude, geo_data.longitude)
        return PromptInformation(geo_data.city, weather_data.temperature, weather_data.description)