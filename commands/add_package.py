from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int
from models.route import Route
from models.truck import Truck

class AddPackage(BaseCommand):
    # appends created package to the list in the selected route: 
    # updates the packages' expected arrival time
    # update the capacity of every route's location along the way of the package 
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 2, 'AddPackage')
        super().__init__(params, app_data)
        
    def execute(self):
        route_id_str, package_id_str = self.params
        route_id = try_parse_int(
            route_id_str, 'Route ID should be an integer number')
        
        route = self.app_data.find_route_by_id(route_id)
        if route.truck == None:
            return 'There is not any truck assigned to the route id #{route_id}'
        
        package_id = try_parse_int(
            package_id_str, 'Package ID should be an integer number')
        package = self.app_data.find_package_by_id(package_id)
        
        start_index, end_index = route.validate_locations(package.start_location, package.end_location)
        if not route.has_capacity(start_index, end_index, package.weight):
            return f"The capacity of the truck is exceeded. Package id #{package._id} cannot be assigned to the route id #{route_id}"
        route._packages.append(package)
        package.route = route
        for i in range(start_index, end_index):
            route.locations[i].capacity -= package.weight  
                                
        package.expected_arrival_time = route.get_expected_arrival_time(package.end_location)
            
        return (f'package #{package._id} was added to the route #{route_id}')
       
       
        
             
        

        

       