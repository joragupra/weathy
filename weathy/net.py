from abc import ABCMeta


class IpAddress(object):
    def __init__(self, ip_address):
        self.ip_address = ip_address


class IpAddressLocator(object):
    __metaclass__ = ABCMeta

    def ip_address_for_local_machine(self):
        pass