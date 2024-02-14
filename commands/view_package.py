from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int

class ViewPackage(BaseCommand):
    
    '''
    print detailed information aboute package:
    1) info() for the required package
    2) route ID, expected current stop 
    '''
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 1, 'ViewPackage')
        super().__init__(params, app_data)
        

    def execute(self):
        package_id_str = self.params[0]
        package_id = try_parse_int(
            package_id_str, 'Package ID should be an integer number')
        package = self.app_data.find_package_by_id(package_id)
        package_info = [f'{package.info()}']
        
        if package.route is None:
            route_info = f"Currently the package id #{package_id} is not assigned to any route"
        else:
            expected_stop = package.route.get_expected_current_stop()    
            route_info = f'Route ID: {package.route._id}, Expected current stop: {expected_stop}\n'

        package_info.append(route_info)

        return "\n".join(package_info)
        
        
        
        