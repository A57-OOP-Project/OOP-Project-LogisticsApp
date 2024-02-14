from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int

class ViewRoute(BaseCommand):
    '''
    print detailed information aboute the specified route
    
    '''
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 1, 'ViewRoute')
        super().__init__(params, app_data)
        

    def execute(self):
        route_id_str = self.params[0]
        route_id = try_parse_int(
            route_id_str, 'Route ID should be an integer number')
        route = self.app_data.find_route_by_id(route_id)
        
        return route.info()
        