from unittest import TestCase
from datetime import datetime
from models.route import Route
from models.truck import Truck
from commands. view_system import ViewSystem
from core.application_data import ApplicationData

ROUTE_ID = 1
TIMEDELTA = 10


class ViewSystem_Should(TestCase):
    
    def setUp(self):
        self.app_data = ApplicationData()
        route_locations = self.app_data.get_estimated_arrival_times(["ASP", "ADL", "MEL"], datetime.now().strftime('%Y-%m-%d %H:%M'))
        self.route = Route(1, route_locations)
        self.truck = Truck('Scania', 1001)
        self.route.truck = self.truck
        for location in self.route.locations:
                location.capacity = self.truck.capacity    
        self.app_data.add_route(self.route)
        self.command = ViewSystem([str(TIMEDELTA)], self.app_data)

   
    def test_executeWithCreatedRoutes(self):
       
        result = self.command.execute()

        expected = '\n'.join([
            f'Route ID: {ROUTE_ID}\n'
            f'{str(self.route)}\n'
            f'Delivery weight: {self.route.get_delivery_weight(TIMEDELTA)}\n'
            f'Expected current stop: {self.route.get_expected_current_stop(TIMEDELTA)}\n'
        ])

        self.assertEqual(expected, result)
