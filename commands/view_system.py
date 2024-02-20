from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int

class ViewSystem(BaseCommand):
    
    '''
    Prints information about all delivery routes in progress:
    it contains route ID, each route's stops, delivery weight, and the expected current stop based on the time of the day
    '''
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 1, 'ViewSystem')
        super().__init__(params, app_data)
     

    def execute(self):
        time_delta_str = self.params[0] #timedelta: hours
        time_delta = try_parse_int(
            time_delta_str, 'TimeDelta should be an integer number')
        all_routes_info = []
        if not self.app_data.routes:
            return 'Currently there are no routes in progress'
        
        for route in self.app_data.routes:
            delivery_weight = route.get_delivery_weight(time_delta)
            expected_current_stop = route.get_expected_current_stop(time_delta)
            route_info = (
                f'Route ID: {route._id}\n'
                f'{str(route)}\n'
                f'Delivery weight: {delivery_weight}\n'
                f'Expected current stop: {expected_current_stop}\n'
               )
            all_routes_info.append(route_info)
            
        return "\n".join(all_routes_info)
        