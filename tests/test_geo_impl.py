import unittest
import weathy.geo_impl

test_ip_api_geo_locator_response = "{\"as\":\"AS31334 Kabel Deutschland Vertrieb und Service GmbH\",\"city\":\"Berlin\",\"country\":\"Germany\",\"countryCode\":\"DE\",\"isp\":\"Kabel Deutschland\",\"lat\":52.5167,\"lon\":13.4,\"org\":\"Kabel Deutschland\",\"query\":\"95.91.213.152\",\"region\":\"BE\",\"regionName\":\"Land Berlin\",\"status\":\"success\",\"timezone\":\"Europe/Berlin\",\"zip\":\"10245\"}"
test_free_geo_ip_response = "{\"ip\":\"95.91.213.152\",\"country_code\":\"DE\",\"country_name\":\"Germany\",\"region_code\":\"NI\",\"region_name\":\"Lower Saxony\",\"city\":\"Hanover\",\"zip_code\":\"30419\",\"time_zone\":\"Europe/Berlin\",\"latitude\":52.367,\"longitude\":9.717,\"metro_code\":0}"


class IpApiGeoLocatorParserTest(unittest.TestCase):
    def test_parser(self):
        geo_location = weathy.geo_impl.IpApiGeoLocatorParser.parse(test_ip_api_geo_locator_response)
        self.assertEqual("Germany", geo_location.country)
        self.assertEqual("Berlin", geo_location.city)
        self.assertEqual(52.5167, geo_location.latitude)
        self.assertEqual(13.4, geo_location.longitude)


class FreeGeoIpGeoLocatorParserTest(unittest.TestCase):
    def test_parse(self):
        geo_location = weathy.geo_impl.FreeGeoIpGeoLocatorParser.parse(test_free_geo_ip_response)
        self.assertEqual("Germany", geo_location.country)
        self.assertEqual("Hanover", geo_location.city)
        self.assertEqual(52.367, geo_location.latitude)
        self.assertEqual(9.717, geo_location.longitude)