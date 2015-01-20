import urllib
import json
from geo import GeoLocator, GeoLocation


class IpApiGeoLocator(GeoLocator):
    def geo_location(self, ip_address):
        return IpApiGeoLocatorParser.parse(urllib.urlopen('http://ip-api.com/json/' + ip_address).read())


class IpApiGeoLocatorParser(object):
    @staticmethod
    def parse(ip_api_response):
        data = json.loads(ip_api_response)
        return GeoLocation(data['city'], data['country'], data['lat'], data['lon'])


class FreeGeoIpGeoLocator(GeoLocator):
    def geo_location(self, ip_address):
        return FreeGeoIpGeoLocatorParser.parse(urllib.urlopen('http://freegeoip.net/json/' + ip_address).read())


class FreeGeoIpGeoLocatorParser(object):
    @staticmethod
    def parse(free_geo_ip_response):
        data = json.loads(free_geo_ip_response)
        return GeoLocation(data['city'], data['country_name'], data['latitude'], data['longitude'])
        