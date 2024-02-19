from unittest import TestCase
from core.application_data import ApplicationData
from datetime import datetime, timedelta
from models.route import Route
from models.truck import Truck
from models.package import Package
from models.location import Location
from models.constants.distances import Distances


class Route_Should(TestCase):
    
    def setUp(self):
        self.app_data = ApplicationData()
        departure_datetime_ASP = datetime.strptime('2024-02-15 16:00', '%Y-%m-%d %H:%M')
        self.location_ASP = Location('ASP', departure_datetime_ASP)
        travel_time_ADL = Distances.calculate_distance(['ASP', 'ADL']) / 87  
        self.arrival_time_ADL = departure_datetime_ASP + timedelta(hours=travel_time_ADL)
        self.location_ADL = Location('ADL', self.arrival_time_ADL)
        travel_time_MEL = Distances.calculate_distance(['ADL', 'MEL']) / 87  
        arrival_time_MEL = self.arrival_time_ADL + timedelta(hours=travel_time_MEL)
        self.location_MEL = Location('MEL', arrival_time_MEL)
        self.locations = [self.location_ASP, self.location_ADL, self.location_MEL]
        self.route = Route(1, self.locations)
        self.app_data.add_route(self.route)
        
    
    def test_initial_setRouteProperties(self):
        
        self.assertEqual(1, self.route.id)
        self.assertEqual(tuple(self.locations), self.route.locations)
        self.assertEqual((), self.route.packages)
        self.assertEqual(None, self.route.truck)
        
        
    def test_truck_setter_raiseErrorWhenInvalidType(self):
        with self.assertRaises(ValueError):
            self.route.truck = 5
            
            
    def test_truck_setter_assignTruckCorrectly(self): 
        
         truck = Truck('Scania', 1001) 
         self.route.truck = truck
         self.assertEqual(truck, self.route.truck)
         
         
    def test__str__returnsCorrectResult(self):
       
        expected_result = (
        f"{self.location_ASP.city} ({self.location_ASP.time.strftime('%Y-%m-%d %H:%M')})" +
        " -> " +
        f"{self.location_ADL.city} ({self.location_ADL.time.strftime('%Y-%m-%d %H:%M')})" +
        " -> " +
        f"{self.location_MEL.city} ({self.location_MEL.time.strftime('%Y-%m-%d %H:%M')})"
    )
         
        self.assertEqual(expected_result, str(self.route))
         
    
    def test_assign_package_raiseErrorWhenAlreadyAssigned(self):
        
        package = Package(1, 'StartLocation', 'EndLocation', 1000, 'ContactInfo')
        self.route.assign_package(package)
        
        with self.assertRaises(ValueError):
            self.route.assign_package(package)
         
    
    def test_assign_package_ifAssignsCorrectly(self):
        
        package = Package(1, 'StartLocation', 'EndLocation', 1000, 'ContactInfo')
        self.route.assign_package(package)
        
        self.assertEqual(1, len(self.route.packages))
        self.assertEqual(package, self.route.packages[0])
        
        
    def test_get_expected_arrival_time_returnsCorrectResult(self):
        
        package = Package(1, 'ASP', 'ADL', 1000, 'ContactInfo')
        self.route.assign_package(package)
        package.route = self.route
        exp_arr_time = self.arrival_time_ADL.strftime('%Y-%m-%d %H:%M')
        
        expected_arrival_time = self.route.get_expected_arrival_time(package.end_location)
        self.assertEqual(exp_arr_time, expected_arrival_time)
        
        
    def test_validate_locations_returnsMessageRouteIsNotSuitable(self):
        
        package_1 = Package(1, 'ADL', 'ASP', 1000, 'ContactInfo') # wrong direction
        
        package_2 = Package(2, 'ASP', 'DAR', 1000, 'ContactInfo') # wrong location
        
        result_msg = f'Route id #{self.route.id} is not suitable for the locations and direction of the package.'
        
        self.assertEqual(result_msg, self.route.validate_locations(package_1.start_location, package_1.end_location))
        self.assertEqual(result_msg, self.route.validate_locations(package_2.start_location, package_2.end_location))
       
        
        
    def test_validate_locations_returnsCorrectResults(self):
        
        package = Package(1, 'ASP', 'ADL', 1000, 'ContactInfo')
        
        result = (0, 1)
        
        self.assertEqual(result, self.route.validate_locations(package.start_location, package.end_location))
        
        
    def test_has_capacity_returnsTrueWhenTruckHasCapacity(self):
        
        truck = Truck('Scania', 1001) 
        
        for location in self.route.locations:
                location.capacity = truck.capacity 
        
        package = Package(1, 'ASP', 'ADL', 1000, 'ContactInfo')
        start_idx, end_idx = self.route.validate_locations(package.start_location, package.end_location)
        
        self.assertTrue(self.route.has_capacity(start_idx, end_idx, package.weight))
        
        
    def test_has_capacity_returnsFalseWhenTruckHasNotEnoughCapacity(self):
        
        truck = Truck('Scania', 1001) 
        
        for location in self.route.locations:
                location.capacity = truck.capacity 
        
        package = Package(1, 'ASP', 'ADL', 50000, 'ContactInfo')
        start_idx, end_idx = self.route.validate_locations(package.start_location, package.end_location)
        
        self.assertFalse(self.route.has_capacity(start_idx, end_idx, package.weight))
        
    
    def test_remove_package_returnsTrueWhenPackageIsRemovedSuccessfully(self):
   
        package = Package(1, 'ASP', 'ADL', 1000, 'ContactInfo')
        self.route.assign_package(package)
        
        self.assertTrue(self.route.remove_package(package.id))
        
       
    def test_remove_package_returnsFalseWhenPackageIsNotInList(self):
   
        package = Package(1, 'ASP', 'ADL', 1000, 'ContactInfo')
       
        self.assertFalse(self.route.remove_package(package.id))
        
        
    def test_get_expected_current_stop_returnsCorrectResultWithZeroTimedelta(self):
        
        self.assertEqual('MEL', self.route.get_expected_current_stop())
        
        
    def test_get_expected_current_stop_returnsCorrectResultWithPositiveTimedelta(self):
        
        self.assertEqual('MEL', self.route.get_expected_current_stop(24))
        
        
    def test_get_delivery_weight_returnsCorrectResult(self):
        
        truck = Truck('Scania', 1001) 
        self.route.truck = truck
        
        self.assertEqual(0, self.route.get_delivery_weight(0))


    def test_info_returnsCorrectResult_whenNoPackagesNoTrucks(self):
        
        result_info = ( f"Route ID: {self.route.id}\nLocations: {str(self.route)}" +
                    "\nNo packages assigned to this route.\n" +
                    "\nNo trucks assigned to this route.\n"
        )
        
        self.assertEqual(result_info, self.route.info())
    
    
    def test_info_returnsCorrectResult_withPackagesAndTrucks(self):
        
        package = Package(1, 'ASP', 'ADL', 1000, 'ContactInfo')
        self.route.assign_package(package)
        
        truck = Truck('Scania', 1001) 
        self.route.truck = truck
        
        result_info = (
          f"Route ID: {self.route.id}\nLocations: {str(self.route)}" +
          "\nAssigned Packages:\n" +
          f"- Package ID: {package.id}, Start Location: {package.start_location}, End Location: {package.end_location}, Weight: {package.weight}kg\n" +
          f"Truck ID: {truck.id}, Name: {truck.name}, Capacity: {truck.capacity}kg, Max Range: {truck.max_range}km\n"
        )
        
