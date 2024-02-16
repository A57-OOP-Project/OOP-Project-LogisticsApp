import unittest
from datetime import datetime
from models.location import Location


class LocationShould(unittest.TestCase):

    def setUp(self):
        self.location = Location("SYD", datetime.now())

    def test_city_immutable(self):
        with self.assertRaises(AttributeError):
            self.location.city = "MEL"

    def test_time_immutable(self):
        with self.assertRaises(AttributeError):
            self.location.time = datetime(2024, 2, 14, 12, 0)

    def test_capacity_changeable(self):
        self.location.capacity = 100
        self.assertEqual(self.location.capacity, 100)