from unittest import TestCase
from core.models_factory import ModelsFactory
from models.package import Package
from models.route import Route
from core.application_data import ApplicationData
from datetime import datetime

class CreatePackage_Should(TestCase):
    
    def test_createValidPackageInstance(self):
      
        start_loc = 'StartLocation'
        end_loc = 'EndLocation'
        weight = 100
        info = 'ContactInfo'
        models_factory = ModelsFactory()

        package = models_factory.create_package(start_loc, end_loc, weight, info)

        self.assertIsInstance(package, Package)
        self.assertEqual(1, package.id)
        self.assertEqual(start_loc, package.start_location)
        self.assertEqual(end_loc, package.end_location)
        self.assertEqual(weight, package.weight)
        self.assertEqual(info, package.contact_info)
        self.assertEqual(None, package.route)
        self.assertEqual(None, package.expected_arrival_time)
        
    def test_createPackagesWithConsecutiveIds(self):
        
        start_loc = 'StartLocation'
        end_loc = 'EndLocation'
        weight = 100
        info = 'ContactInfo'
        models_factory = ModelsFactory()

        package_1 = models_factory.create_package(start_loc, end_loc, weight, info)
        package_2 = models_factory.create_package(start_loc, end_loc, weight, info)
        package_3 = models_factory.create_package(start_loc, end_loc, weight, info)

        self.assertEqual(1, package_1.id)
        self.assertEqual(2, package_2.id)
        self.assertEqual(3, package_3.id)    
    
    
class CreateRoute_Should(TestCase):
    
    def test_createValidRouteInstance(self):
        
        self.app_data = ApplicationData()
        models_factory = ModelsFactory()
        locations = self.app_data.get_estimated_arrival_times(["ASP", "ADL", "MEL"], datetime.now().strftime('%Y-%m-%d %H:%M'))
        locations_tuple = tuple(locations)
        route = models_factory.create_route(locations)
   
        self.assertIsInstance(route, Route)
        self.assertEqual(1, route.id)
        self.assertEqual(locations_tuple, route.locations)
        self.assertEqual((), route.packages)
        self.assertEqual(None, route.truck)
        
        
    def test_createRoutesWithConsecutiveIds(self):
        
        self.app_data = ApplicationData()
        models_factory = ModelsFactory()
        route1_locations = self.app_data.get_estimated_arrival_times(["ASP", "ADL", "MEL"], datetime.now().strftime('%Y-%m-%d %H:%M'))
        route2_locations = self.app_data.get_estimated_arrival_times(["MEL", "SYD", "BRI"], datetime.now().strftime('%Y-%m-%d %H:%M'))
        route3_locations = self.app_data.get_estimated_arrival_times(["BRI", "ASP", "PER"], datetime.now().strftime('%Y-%m-%d %H:%M'))
        
        route_1 = models_factory.create_route(route1_locations)
        route_2 = models_factory.create_route(route2_locations)
        route_3 = models_factory.create_route(route3_locations)
        
        self.assertEqual(1, route_1.id)
        self.assertEqual(2, route_2.id)
        self.assertEqual(3, route_3.id)    


