from unittest import TestCase
from core.application_data import ApplicationData
from datetime import datetime, timedelta
from models.route import Route
from models.truck import Truck
from models.package import Package
from models.location import Location
from models.constants.distances import Distances
from models.schedule import Schedule


class ApplicationData_Should(TestCase):
    
    def test_assignEmptysRoutesPackagesAndTrucksCollections(self):
        
        self.app_data = ApplicationData()
        self.assertEqual((), self.app_data.routes)
        self.assertEqual((), self.app_data.packages)
        self.assertEqual((), self.app_data.trucks)
        
    
    def setUp(self):
        self.app_data = ApplicationData()
        self.truck = Truck('Scania', 1001)
        self.app_data.add_truck(self.truck)
        departure_datetime_ASP = datetime.strptime('2024-02-18 16:00', '%Y-%m-%d %H:%M')
        location_ASP = Location('ASP', departure_datetime_ASP)
        travel_time_ADL = Distances.calculate_distance(['ASP', 'ADL']) / 87  
        arrival_time_ADL = departure_datetime_ASP + timedelta(hours=travel_time_ADL)
        location_ADL = Location('ADL', arrival_time_ADL)
        travel_time_MEL = Distances.calculate_distance(['ADL', 'MEL']) / 87  
        arrival_time_MEL = arrival_time_ADL + timedelta(hours=travel_time_MEL)
        location_MEL = Location('MEL', arrival_time_MEL)
        locations = [location_ASP, location_ADL, location_MEL]
        self.route = Route(1, locations)
        self.app_data.add_route(self.route)
        self.package = Package(1, 'StartLocation', 'EndLocation', 1000, 'ContactInfo')
        self.app_data.add_package(self.package)
        
        

    def test_addTruckReturnsCorrectResult(self):
        
        self.assertEqual(len(self.app_data.trucks), 1)
        self.assertIn(self.truck, self.app_data.trucks)
        
    def test_addTruckRaiseErrorIfTruckAlreadyAdded(self):
      
        with self.assertRaises(ValueError):
            self.app_data.add_truck(self.truck)
            
            
    def test_addRouteReturnsCorrectResult(self):
        
        self.assertEqual(len(self.app_data.routes), 1)
        self.assertIn(self.route, self.app_data.routes)
        
        
    def test_addRouteRaiseErrorIfRouteAlreadyAdded(self):
      
        with self.assertRaises(ValueError):
            self.app_data.add_route(self.route)
             
    
    def test_addPackageReturnsCorrectResult(self):
        
        self.assertEqual(len(self.app_data.packages), 1)
        self.assertIn(self.package, self.app_data.packages)
        
    def test_addPackageRaiseErrorIfPackageAlreadyAdded(self):
      
        with self.assertRaises(ValueError):
            self.app_data.add_package(self.package)

   
    def test_find_truck_by_idReturnsCorrectResult(self):
       
        found_truck = self.app_data.find_truck_by_id(1001)
        self.assertEqual(self.truck, found_truck)
        
    def test_find_truck_by_idRaiseErrorIfInvalidTruckId(self):
      
        with self.assertRaises(ValueError):
            self.app_data.find_truck_by_id(1000)
    

    def test_find_route_by_idReturnsCorrectResult(self):
       
        found_route = self.app_data.find_route_by_id(1)
        self.assertEqual(self.route, found_route)
        
    def test_find_route_by_idRaiseErrorIfInvalidRouteId(self):
      
        with self.assertRaises(ValueError):
            self.app_data.find_route_by_id(10)
       

    def test_find_package_by_idReturnsCorrectResult(self):
        
        found_package = self.app_data.find_package_by_id(1)
        self.assertEqual(self.package, found_package)
        
    def test_find_package_by_idRaiseErrorIfInvalidPackageId(self):
      
        with self.assertRaises(ValueError):
            self.app_data.find_package_by_id(10)
    
  
    def test_is_truck_assignedReturnsTrueIfAssigned(self):
        
        self.assertTrue(self.app_data.is_truck_assigned(1001))
        

    def test_is_truck_assignedReturnFalseIfUnassigned(self):
        
        self.assertFalse(self.app_data.is_truck_assigned(1002))
        
        
    def test_find_suitable_trucksReturnsCorrectResult(self):
        Schedule.add_route(1001, 1)  
        suitable_trucks = [1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
        
        involved_trucks = involved_trucks = [
            f'Route id #1: {self.route.locations[0].city} ({self.route.locations[0].time.strftime('%Y-%m-%d %H:%M')}) -> '
            f'{self.route.locations[1].city} ({self.route.locations[1].time.strftime('%Y-%m-%d %H:%M')}) -> '
            f'{self.route.locations[2].city} ({self.route.locations[2].time.strftime('%Y-%m-%d %H:%M')})'
        ]
        
        unsuitable_trucks = {'MAN', 'ACTROS'}
        
        suitable_available_trucks, suitable_involved_trucks, unsuitable_trucks_names = self.app_data.find_suitable_trucks(40000, 6000)
        self.assertTrue(isinstance(suitable_available_trucks, list))
        self.assertTrue(isinstance(suitable_involved_trucks, list))
        self.assertTrue(isinstance(unsuitable_trucks_names, set))
        self.assertEqual(suitable_available_trucks, suitable_trucks)
        self.assertEqual(suitable_involved_trucks, involved_trucks)
        self.assertEqual(unsuitable_trucks_names, unsuitable_trucks)
    
    
    def test_get_estimated_arrival_timesReturnsCorrectResult(self):
        
        locations_strings = ['ASP', 'ADL', 'MEL']
        departure_time = '2024-02-18 16:00'
        locations_of_route = self.app_data.get_estimated_arrival_times(locations_strings, departure_time)
        self.assertTrue(isinstance(locations_of_route, list))
        self.assertEqual(len(locations_of_route), len(locations_strings))
        for i in range(len(locations_of_route)):
            self.assertEqual(self.route.locations[i].city, locations_of_route[i].city)
            self.assertEqual(self.route.locations[i].time, locations_of_route[i].time)
             
        
    
    def test_is_schedule_conflictReturnsCorrectResult(self):
        Schedule.add_route(1001, 1)  
        routes = []
        departure_datetime = [datetime.strptime('2024-02-18 16:00', '%Y-%m-%d %H:%M'), datetime.strptime('2024-02-25 16:00', '%Y-%m-%d %H:%M')]
        for i in range(len(departure_datetime)):
            location_MEL = Location('MEL', departure_datetime[i])
            travel_time_SYD = Distances.calculate_distance(['MEL', 'SYD']) / 87  
            arrival_time_SYD = departure_datetime[i] + timedelta(hours=travel_time_SYD)
            location_SYD = Location('SYD', arrival_time_SYD)
            locations = [location_MEL, location_SYD]
            route = Route(i + 2, locations)
            self.app_data.add_route(route)
            routes.append(route)

        self.assertTrue(self.app_data.is_schedule_conflict(1001, routes[0].id))
        self.assertFalse(self.app_data.is_schedule_conflict(1001, routes[1].id))
        
        
    
                             

    
    
    
    
        

    
         
    