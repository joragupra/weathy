import json
import urllib
from net import IpAddressLocator, IpAddress


class JsonTestServiceIpAddressLocator(IpAddressLocator):
    def ip_address_for_local_machine(self):
        data = json.loads(urllib.urlopen('http://ip.jsontest.com/').read())
        return IpAddress(data["ip"])