import unittest
from unittest.mock import patch
from models.constants.truck_types import TruckTypes


class TruckTypes_Should(unittest.TestCase):
    def test_format_truck_info(self):
        # suitable and unsuitable trucks for testing
        suitable_trucks = [1001, 1003, 1015, 1027, 1035]
        unsuitable_trucks = {'MAN'}  # 'MAN' trucks are unsuitable for this test

        with patch.object(TruckTypes, 'DATA', {
            'SCANIA': {'capacity': 42000, 'max_range': 8000},
            'MAN': {'capacity': 37000, 'max_range': 10000},
            'ACTROS': {'capacity': 26000, 'max_range': 13000}
        }):
            expected_output = (
                "Available trucks with appropriate capacity and range:\n"
                "Name: Scania, Capacity: 42000 kg, Max Range: 8000 km\nTruck IDs: 1001, 1003\n"
                "Name: Actros, Capacity: 26000 kg, Max Range: 13000 km\nTruck IDs: 1027, 1035\n"
            )
            output = TruckTypes.format_truck_info(suitable_trucks, unsuitable_trucks)
            self.assertEqual(output, expected_output)