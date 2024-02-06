from datetime import datetime, timedelta


class Route:
    def __init__(self, id, locations: list):
        self._id = id 
        self._packages = []
        self._trucks = []
        # self._locations: list[tuple[str, datetime]] = [] #  [(location_1, departure_time), (location_2), arrival_time)]
        self._locations = locations

    @property
    def id(self):
        return self._id
    
    @property
    def locations(self):
        return self._locations
    
    @locations.setter
    def locations(self,value):
        self.ensure_locations_is_valid(value)
        self._locations.append(value)
        print(value)
        return self._locations

    def ensure_locations_is_valid(self,locations):
        if (
            isinstance(locations, tuple) and 
            len(locations) == 2 and 
            isinstance(locations[0], (str, int)) and 
            isinstance(locations[1], datetime)
            ):
            return True
        raise ValueError('Invalid location format')

    def calculate_route_distance(self):
        '''Depends on constants.distances when the matrix is ready'''
        pass

    def add_truck(self, truck):
        if truck not in self._trucks:
            return self._trucks.append(truck)
        pass

    def assign_package(self, package):
        if package not in self._packages:
            return self._packages.append(package)
        pass
    
    def __str__(self) -> str:
        stops: list = []
        next_stop = ''
        # Check if route is in progress/active
        if len(self._packages) > 0 and len(self._trucks) > 0:
            pass
        #Add all the stops. Should they be all or remaining?
        for key in self._locations:
            stops.append(key[0])
                # #Add total_delivery_weight calc - is ._weight ready in models.package? import models.Package once ready. Create a test.
                # delivery_weight: int = 0
                # for i in self._packages:
                #     delivery_weight += i._weight
        #Add next stop based on time of day
        time_now = datetime.now(tz=None) 
        for arrival_time_at_stop in self._locations:
            if arrival_time_at_stop > time_now:
                next_stop = arrival_time_at_stop 
                break
        return '\n'.join([
            f'Delivery stops left: {stops}',
            f'Delivery weight: delivery weight to be added',
            f'Next stop is: {next_stop}'
            ])

    def display_route(self):
        #What is this def for? 
        pass

route = Route(id=1, locations=("Location1", datetime(2024, 2, 5, 10, 30)))
print(route.locations)
print(route.__str__())