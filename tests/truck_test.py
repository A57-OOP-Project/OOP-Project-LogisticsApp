import unittest
from models.truck import Truck

class Truck_Should(unittest.TestCase):
    correct_truck = Truck('scania',1001)
    
    def test_initialiser_whenAllDataIsCorrect(self):
        name = 'scania'
        truck_id = 1001
        truck1 = Truck(name,truck_id)
        self.assertEqual(truck1.name, name)
        self.assertEqual(truck1.id, truck_id)
        self.assertIsInstance(name,str)
        self.assertIsInstance(truck_id,int)

    def test_raiseValueError_whenTruckIdIsIncorrect(self):
        name = 'SCANIA'
        truck_id = 1 #number otside of 1001-1040 range
        with self.assertRaises(ValueError):
            Truck(name,truck_id)

    def test_raiseValueError_whenTrucknameIsEmpty(self):
        name = ''
        truck_id = 1001 
        with self.assertRaises(ValueError):
            Truck(name,truck_id)

    def test_raiseValueError_whenTrucknameIsDifferentThanTheAllowed(self):
        name = 'MERCEDES'
        truck_id = 1001 
        with self.assertRaises(ValueError):
            Truck(name,truck_id)

    def test_raiseValueError_whenWhenInvalidID(self):
        name = 'MAN'
        truck_id = 1001
        with self.assertRaises(ValueError):
            Truck(name,truck_id)

    def test_raiseAttributeError_whenReadOnlyPropertyNAMEIsTryingToChange(self):
        with self.assertRaises(AttributeError):
            self.correct_truck.name = 'man'

    def test_raiseAttributeError_whenReadOnlyPropertyIDIsTryingToChange(self):
        with self.assertRaises(AttributeError):
            self.correct_truck.id = 1001

    def test_raiseAttributeError_whenReadOnlyPropertyCapacityIsTryingToChange(self):
        with self.assertRaises(AttributeError):
            self.correct_truck.capacity = 1000

    def test_raiseAttributeError_whenReadOnlyPropertyMaxRangeIsTryingToChange(self):
        with self.assertRaises(AttributeError):
            self.correct_truck.max_range = 1000

    def test_infomethod_hasCorrectOutput(self):
        self.assertEqual("Truck ID: 1001\nName: scania\nCapacity: 42000 kg\nMax Range: 8000 km",f"Truck ID: {self.correct_truck.id}\nName: {self.correct_truck.name}\nCapacity: {self.correct_truck.capacity} kg\nMax Range: {self.correct_truck.max_range} km")

