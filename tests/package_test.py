import unittest
from models.package import Package


class PackageShould(unittest.TestCase):
    def setUp(self):
        self.package = Package(
            id=123,
            start_location="SYD",
            end_location="MEL",
            weight=5000,
            contact_info="Pesho"
        )

    def test_properties(self):
        self.assertEqual(self.package.id, 123)
        self.assertEqual(self.package.start_location, "SYD")
        self.assertEqual(self.package.end_location, "MEL")
        self.assertEqual(self.package.weight, 5000)
        self.assertEqual(self.package.contact_info, "Pesho")
        self.assertIsNone(self.package.expected_arrival_time)

    def test_expected_arrival_time(self):
        self.package.expected_arrival_time = "2024-02-14 12:00"
        self.assertEqual(self.package.expected_arrival_time, "2024-02-14 12:00")

    def test_info_no_route_assigned(self):
        expected_info = f"Package ID: {self.package.id}\n" \
                        f"Start Location: {self.package.start_location}\n" \
                        f"End Location: {self.package.end_location}\n" \
                        f"Weight: {self.package.weight} kg\n" \
                        f"Contact Info: {self.package.contact_info}\n" \
                        f"Currently the package id #{self.package.id} is not assigned to any route"
        self.assertEqual(self.package.info(), expected_info)

    def test_info_with_route_assigned(self):
        self.package.expected_arrival_time = "2024-02-14 12:00"
        self.package.route = "SYD-MEL"  # Dummy route for testing
        expected_info = f"Package ID: {self.package.id}\n" \
                        f"Start Location: {self.package.start_location}\n" \
                        f"End Location: {self.package.end_location}\n" \
                        f"Weight: {self.package.weight} kg\n" \
                        f"Contact Info: {self.package.contact_info}\n" \
                        f"Expected Arrival Time: {self.package.expected_arrival_time}"
        self.assertEqual(self.package.info(), expected_info)

    def test_id_immutable(self):
        with self.assertRaises(AttributeError):
            self.package.id = 456

    def test_weight_immutable(self):
        with self.assertRaises(AttributeError):
            self.package.weight = 6000
# the two tests above check whether trying to change the id and weight raises errors

    def test_start_location_changeable(self):
        self.package.start_location = "ADL"
        self.assertEqual(self.package.start_location, "ADL")

    def test_end_location_changeable(self):
        self.package.end_location = "ASP"
        self.assertEqual(self.package.end_location, "ASP")

    def test_contact_info_changeable(self):
        self.package.contact_info = "Misho"
        self.assertEqual(self.package.contact_info, "Misho")

    def test_expected_arrival_time_changeable(self):
        self.package.expected_arrival_time = "2024-02-15 14:00"
        self.assertEqual(self.package.expected_arrival_time, "2024-02-15 14:00")

    def test_route_changeable(self):
        self.package.route = "ADL-ASP"
        self.assertEqual(self.package.route, "ADL-ASP")
# the tests above check whether route, contact and arrival time can be changed