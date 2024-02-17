from unittest import TestCase
from models.constants.truck_types import TruckTypes
from models.truck import Truck

class TruckTypes_should(TestCase):
    # def test_truckinfo_validOutput(self):
    #     # truck = Truck('SCANIA', 1001)
    #     self.assertEqual("Name: SCANIA, Capacity: 42000 kg, Max Range: 8000 km\nTruck IDs: 1001,1002,1003,1004,1005,1006,1007,1008,1009,1010)",f"Name: {TruckTypes.truck_type}, Capacity: {TruckTypes.DATA[TruckTypes.format_truck_info.truck_type.upper()]['capacity']} kg, Max Range: {TruckTypes.DATA[TruckTypes.format_truck_info.truck_type.upper()]['max_range']} km\nTruck IDs: {', '.join(map(str, TruckTypes.truck_ids))}")

    # # def check_truckinfoIDs_areValidnumbers(self):
