from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int
from models.truck import Truck
from models.route import Route
from models.schedule import Schedule

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
        result_str = ''
        route = self.app_data.find_route_by_id(route_id)
        if route.truck != None:
            result_str = f'To the route id #{route_id} currently is assigned truck id #{route.truck.id}. The truck reassignment is expected\n'
         
        if not self.app_data.is_truck_assigned(truck_id):
            new_truck = Truck(name, truck_id)
            self.app_data.add_truck(new_truck)
            route.truck = new_truck
            for location in route.locations:
                location.capacity = new_truck.capacity
        else:
            if self.app_data.is_schedule_conflict(truck_id, route_id):
                return f'Schedule conflict: routes time ranges overlap. Truck id #{truck_id} cannot be assigned to the route id #{route_id}'    
            truck = self.app_data.find_truck_by_id(truck_id)
            route.truck = truck
            for location in route.locations:
                location.capacity = truck.capacity  
                        
        Schedule.add_route(truck_id, route_id)  
        
        result_str += f'Truck id #{truck_id} is assigned to the route id #{route_id}'              
        return result_str
