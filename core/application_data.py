from models.constants.distances import Distances
from datetime import datetime, timedelta
from models.package import Package
from models.route import Route
from models.truck import Truck
from models.constants.truck_types import TruckTypes

class ApplicationData:
    def __init__(self):
        self._routes = []
        self._packages = []
        self._trucks = []


    @property
    def packages(self):
        return tuple(self._packages)
    
    @property
    def trucks(self):
        return tuple(self._trucks)
    
    
    @property
    def routes(self):
        return tuple(self._routes)
    

    def add_truck(self, truck):
        if truck not in self._trucks:
            self._trucks.append(truck)
        else:
            raise ValueError("The truck has been already added")

             
    def add_route(self, route):
        if route not in self._routes:
            self._routes.append(route)
        else:
            raise ValueError("The route has been already added")

    def add_package(self, package):
        if package not in self._packages:
            self._packages.append(package)
        else:
            raise ValueError("The package has been already added")

        
    def find_package_by_id(self, pack_id) -> Package:
        for package in self._packages:
            if package._id == pack_id:
                return package

        raise ValueError(f'Package with id #{pack_id} does not exist!')
    
    def find_route_by_id(self, r_id) -> Route:
        for route in self._routes:
            if route._id == r_id:
                return route
            
    def is_truck_assigned(self, id) -> bool:
        return id in [truck._id for truck in self._trucks]
    
    def find_route_by_package_id(self, pack_id):
        for route in self._routes:
                for package in route.packages:
                    if package._id == pack_id:
                        return route
        return None
    
    def get_estimated_arrival_times(self, locations: list[str], departure_time: str): #departure_time is a string in format 'YYYY-MM-DD HH:MM'
        
        #departure_datetime = datetime.strptime(departure_time, '%Y-%m-%d %H:%M')
        try:
            departure_datetime = datetime.strptime(departure_time, '%Y-%m-%d %H:%M')
        except ValueError:
            raise ValueError("Invalid format for departure time. Please use 'YYYY-MM-DD HH:MM'")

        estimated_arrival_times = []
        estimated_arrival_times.append((locations[0], departure_datetime))
        
        for i in range(1, len(locations)):
            current_time = estimated_arrival_times[-1][1]
            location = locations[i]
            travel_time = Distances.calculate_distance(locations[i-1:i+1]) / 87  #average speed is 87 km/h
            arrival_time = current_time + timedelta(hours=travel_time)
            estimated_arrival_times.append((location, arrival_time))
            
        return estimated_arrival_times
     
        
    def find_suitable_trucks(self, packages_weight, route_distance):
        suitable_trucks = []
        for truck_type, truck_info in TruckTypes.DATA.items():
            if truck_info['capacity'] >= packages_weight and truck_info['max_range'] >= route_distance:
                truck_ids = range(truck_info['ids_min'], truck_info['ids_max'] + 1)
                for truck_id in truck_ids:
                    if not self.is_truck_assigned(truck_id):
                        suitable_trucks.append(truck_id)
        return suitable_trucks
    
    