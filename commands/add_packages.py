from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import try_parse_int
from models.route import Route
from models.truck import Truck

class AddPackages(BaseCommand):
    # takes in a variable number of arguments(packages_ids)
    # appends created packages to the list in the selected route: 
    # updates the packages' expected arrival time
    # update capacity of the truck 
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        #without validate_params_count() because it takes in a variable number of arguments
        super().__init__(params, app_data)
        
    def execute(self):
        msg = []
        total_weight = 0
        route_id_str, *packages_ids = self.params
        route_id = try_parse_int(
            route_id_str, 'Route ID should be an integer number')
        route = self.app_data.find_route_by_id(route_id)
        truck = route.trucks[0]
                
        for package_id_str in packages_ids: 
            package_id = try_parse_int(
            package_id_str, 'Package ID should be an integer number')
            package = self.app_data.find_package_by_id(package_id)
            total_weight += package.weight
            if truck.capacity < total_weight:
               return "The capacity of the truck is exceeded. Package id #{package._id} cannot be assigned to the route"
            route.assign_package(package)
            package.expected_arrival_time = route.get_expected_arrival_time(package.end_location)
            msg.append(f'package #{package._id} was added tо the route #{route_id}')
        
        truck.capacity -= total_weight 
        return "\n".join(msg)

""" before adding packages to the existing route(i.e. not new, not just created route) it's necessary to check if the route's truck
    has enough capacity to accommodate the total weight of the packages. So in the console before AddPackages command we should use
    some_route.check_capacity(self, start_location_of_parcels, end_location_of_parcels, weight_of_parcels) 
"""
        

       