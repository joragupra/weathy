import socket, urllib, json


class Netlocator(object):
    def __init__(self):
        """Do nothing here"""

    def ipaddress(self):
        data = json.loads(urllib.urlopen('http://ip.jsontest.com/').read())
        return data["ip"]


class Geolocator(object):
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    def city(self, ipaddress=None):
        if ipaddress == None:
            ipadd = self.ipaddress
        else:
            ipadd = ipaddress
        data = json.loads(urllib.urlopen('http://freegeoip.net/json/' + ipadd).read())
        return data["city"]

    def geolocation(self, ipaddress=None):
        if ipaddress == None:
            ipadd = self.ipaddress
        else:
            ipadd = ipaddress
        data = json.loads(urllib.urlopen('http://freegeoip.net/json/' + ipadd).read())
        return data