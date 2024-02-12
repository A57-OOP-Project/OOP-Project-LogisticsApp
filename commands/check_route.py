from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from datetime import datetime
from models.route import Route
from commands.validation_helpers import validate_params_count, try_parse_int

class CheckRouteCapacity(BaseCommand):
    '''
    Calculates capacity that the truck will have in each location along the route of a given parcel.
    Returns relevant messages: "there are capacity"-if in all locations the truck will have the required capacity 
    or "there are not capacity" - if at least in one of the locations along the route of this parcel the truck 
    will not have the required capacity
    
    '''
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 4, 'CheckRouteCapacity')
        super().__init__(params, app_data)
        
    def execute(self):
        route_id_str, start_location, end_location, weight_str = self.params
        route_id = try_parse_int(
            route_id_str, 'Route ID should be an integer number')
        weight = try_parse_int(
            weight_str, 'Weight should be an integer number')
        route = self.app_data.find_route_by_id(route_id)
        if route.check_capacity(start_location, end_location, weight):
            return f'Route #{route.id} has required capacity for the specified weight' 
        else:
            return f'Route #{route.id} has not required capacity for the specified weight'  