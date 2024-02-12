from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int

class RemovePackageFromRoute(BaseCommand):
    '''
    removes package from route, but not from app_data.packages
    
    '''
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 2, 'RemovePackageFromRoute')
        super().__init__(params, app_data)
        
    def execute(self):
        route_id_str, pack_id_str = self.params
        route_id = try_parse_int(
            route_id_str, 'Route ID should be an integer number')
        package_id = try_parse_int(
            pack_id_str, 'Package ID should be an integer number')
        route = self.app_data.find_route_by_id(route_id)
        if route.remove_package(package_id):
            return f'Package #{package_id} was removed from route #{route_id}'
        else:
            return f'Package #{package_id} is not found'
        

        