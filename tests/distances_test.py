import unittest
from models.constants.distances import Distances


class Distances_Should(unittest.TestCase):
    def test_calculate_distance_isValid(self):
        locations = ["MEL", "BRI"]
        distance = Distances.calculate_distance(locations)
        self.assertEqual(1765, distance)
