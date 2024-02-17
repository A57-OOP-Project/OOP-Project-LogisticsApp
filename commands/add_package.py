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
        
        # Check if the route exists in the application data
        route = self.app_data.find_route_by_id(route_id)
        # Checks if the route has a truck assigned 
        if route.truck == None:
            return 'There is not any truck assigned to the route id #{route_id}'
        
        package_id = try_parse_int(
            package_id_str, 'Package ID should be an integer number')
        # Find the previously created package in the application data
        package = self.app_data.find_package_by_id(package_id)
        # Check 
        start_index, end_index = route.validate_locations(package.start_location, package.end_location) # Q - does it check for the correct route_id? Does it refer to the route on line 21?
        # Checks for capacity on the route to which the package is being added
        if not route.has_capacity(start_index, end_index, package.weight):
            return f"The capacity of the truck is exceeded. Package id #{package._id} cannot be assigned to the route id #{route_id}"
        # Add package to route since we have: checked route and package exist, checked if truck assigned, check if package in direction of the route_id and capacity on each location, so we add it:
        # Add package to models.route
        route._packages.append(package)
        # Add the route to the package
        package.route = route
        # Reduce capacity on each location by the package's weight
        for i in range(start_index, end_index):
            route.locations[i].capacity -= package.weight 
        # Calculates and assigns the expected arrival time of the package based on the route
        package.expected_arrival_time = route.get_expected_arrival_time(package.end_location)
            
        return (f'package #{package._id} was added to the route #{route_id}')
       
       
        
             
        

        

       