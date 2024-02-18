import unittest
from datetime import datetime
from models.route import Route
from models.truck import Truck
from models.location import Location
from models.package import Package


class RouteShould(unittest.TestCase):
    def setUp(self):
        # locations of the route
        self.location1 = Location("SYD", datetime(2024, 2, 17, 8, 0))
        self.location2 = Location("MEL", datetime(2024, 2, 17, 12, 0))
        self.location3 = Location("ADL", datetime(2024, 17, 16, 0))

        self.truck = Truck("Truck1", 26000)

        self.package1 = Package(1, "SYD", "MEL", 1000, "Pesho")
        self.package2 = Package(2, "MEL", "ADL", 2000, "Pesho")

        self.route = Route(1, [self.location1, self.location2, self.location3])

    def test_get_expected_arrival_time(self):
        self.assertEqual(self.route.get_expected_arrival_time("SYD"), "2024-02-17 08:00")
        self.assertEqual(self.route.get_expected_arrival_time("MEL"), "2024-02-17 12:00")
        self.assertEqual(self.route.get_expected_arrival_time("ADL"), "2024-02-17 16:00")
        self.assertIsNone(self.route.get_expected_arrival_time("BRI"))  # non-existing city for the route

    def test_validate_locations(self):
        self.assertEqual(self.route.validate_locations("SYD", "ADL"), (0, 2))  # valid start and end locations
        self.assertIsNone(self.route.validate_locations("SYD", "BRI"), "Route id #1 is not suitable for the locations and direction of the package.")  # invalid end location
        self.assertIsNone(self.route.validate_locations("BRI", "ADL"), "Route id #1 is not suitable for the locations and direction of the package.")  # invalid start location
        self.assertIsNone(self.route.validate_locations("BRI", "DAR"), "Route id #1 is not suitable for the locations and direction of the package.")  # invalid locations

    def test_has_capacity(self):
        self.assertTrue(self.route.has_capacity(0, 2, 3000))  # enough capacity
        self.assertFalse(self.route.has_capacity(0, 2, 60000))  # not enough capacity

    def test_assign_package(self):
        self.route.assign_package(self.package1)
        self.assertIn(self.package1, self.route.packages)  # assigned package

    def test_remove_package(self):
        self.route.assign_package(self.package1)
        self.assertTrue(self.route.remove_package(1))
        self.assertNotIn(self.package1, self.route.packages)  # package not in packages list

    def test_get_expected_current_stop(self):
        # current time is before any location time
        self.assertEqual(self.route.get_expected_current_stop(), "SYD")

        # current time is between SYD and MEL times
        self.current_time = datetime(2024, 2, 17, 10, 0)
        self.assertEqual(self.route.get_expected_current_stop(), "MEL")

        # current time is after final stop
        self.current_time = datetime(2024, 2, 17, 16, 0)
        self.assertEqual(self.route.get_expected_current_stop(), "ADL")

    def test_get_delivery_weight_before_any_location_time(self):                                                #????
        delivery_weight = self.route.get_delivery_weight(-1)  # simulating 1 hour before the first location
        self.assertEqual(delivery_weight, 26000)

    def test_get_delivery_weight_between_location_times(self):
        delivery_weight = self.route.get_delivery_weight(2)  # simulating 10:00
        self.assertEqual(delivery_weight,
                         25000)

    def test_get_delivery_weight_after_final_stop(self):
        delivery_weight = self.route.get_delivery_weight(8)  # simulating 16:00
        self.assertEqual(delivery_weight, 26000)



