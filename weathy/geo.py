from abc import ABCMeta


class GeoLocation(object):
    def __init__(self, city, country, lat, lon):
        self.city = city
        self.country = country
        self.latitude = lat
        self.longitude = lon


class GeoLocator(object):
    __metaclass__ = ABCMeta

    def geo_location(self, ip_address):
        pass