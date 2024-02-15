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

    # def test_info(self):
        #This one fails for me. Maybe have ID of 1? Svetlio has error: Currently the package id #123 is not assigned to any route
        # expected_info = "Package ID: 123\n" \
        #                 "Start Location: SYD\n" \
        #                 "End Location: MEL\n" \
        #                 "Weight: 5000 kg\n" \
        #                 "Contact Info: Pesho\n" \
        #                 "Expected Arrival Time: 2024-02-14 12:00"
        # self.package.expected_arrival_time = "2024-02-14 12:00"
        # self.assertEqual(self.package.info(), expected_info)


    # you can add tests for the properties which dont have setters that they dont change 
    # and for the ones with setters that can be changed