from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from datetime import datetime
from models.route import Route
from commands.validation_helpers import validate_params_count, try_parse_int

class CheckRouteCapacity(BaseCommand):
    
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 4, 'CheckRouteCapacity') 
        super().__init__(params, app_data)
      
    def execute(self):
        '''
        Checks whether a given route has the required capacity for a specified weight.
        '''
        route_id_str, start_location, end_location, weight_str = self.params
        route_id = try_parse_int(
            route_id_str, 'Route ID should be an integer number')
        weight = try_parse_int(
            weight_str, 'Weight should be an integer number')
        route = self.app_data.find_route_by_id(route_id) #route lookup
        if route.truck == None: #truck assignment check
            return 'There is not any truck assigned to the route id #{route_id}'
        
        start_index, end_index = route.validate_locations(start_location, end_location) #returns start and end indices of the locations along the route
        if route.has_capacity(start_index, end_index, weight): #check if the route has the required capacity to carry the specified weight
            return f'Route #{route.id} has required capacity for the specified weight' 
        else:
            return f'Route #{route.id} has not required capacity for the specified weight'  
        
       