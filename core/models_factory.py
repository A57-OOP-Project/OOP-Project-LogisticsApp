from models.package import Package
from models.route import Route

class ModelsFactory: 
    #contains methods for creating instances of Package and Route 
    def __init__(self):
        self._package_id = 1
        self._route_id = 1

    def create_package(self, start_location: str, end_location: str, weight: int, contact_info: str):
        '''
        Creates a new Package object with specified attributes
        '''
        package_id = self._package_id
        self._package_id += 1

        return Package(package_id, start_location, end_location, weight, contact_info)

    def create_route(self, route_locations: list):
        '''
        Creates a new Route object with specified locations along the route
        '''
        route_id = self._route_id
        self._route_id += 1

        return Route(route_id, route_locations)
    