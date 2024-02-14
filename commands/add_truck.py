from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int
from models.truck import Truck
from models.route import Route

class AddTruck(BaseCommand):
    #creates an instance of class Truck 
    #appends created truck to the list in the selected route and to the corresponding list in ApplicationData 
    
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 3, 'AddTruck')
        super().__init__(params, app_data)
        
    def execute(self):
        name, truck_id_str, route_id_str = self.params
        route_id = try_parse_int(
            route_id_str, 'Route ID should be an integer number')
        truck_id = try_parse_int(
            truck_id_str, 'Truck ID should be an integer number')
        truck = Truck(name, truck_id)
        self.app_data.add_truck(truck)
        route = self.app_data.find_route_by_id(route_id)
        route.truck = truck
        for location in route.locations:
            location.capacity = truck.capacity
        
        return f'Truck id #{truck_id} was added to the route id #{route_id}'

