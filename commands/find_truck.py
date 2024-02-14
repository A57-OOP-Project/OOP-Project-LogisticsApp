from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int
from models.constants.distances import Distances
from models.constants.truck_types import TruckTypes

class FindTruck(BaseCommand):
    '''
        finds a free truck that meets the required range and capacity
               
        '''
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
       #without validate_params_count() because it takes in a variable number of arguments(locations)
        super().__init__(params, app_data)
        
        
    def execute(self):
        weight_str = self.params[0]
        locations = self.params[1:]
        packages_weight = try_parse_int(
            weight_str, 'Weight should be an integer number')
        route_distance = Distances.calculate_distance(locations)
        suitable_trucks, unsuitable_trucks = self.app_data.find_suitable_trucks(packages_weight, route_distance)
        if not suitable_trucks:
            return "No suitable trucks were found"
        
        return TruckTypes.format_truck_info(suitable_trucks, unsuitable_trucks)

    
    
    