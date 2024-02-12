from datetime import datetime
from models.package import Package
from models.truck import Truck
from commands.validation_helpers import try_parse_int

class Route:
    def __init__(self, id, locations: list):
        self._id = id 
        self._packages = []
        self._trucks = []
        self._locations = locations #  [(location_1, departure_time), (location_2), arrival_time)]
    
    @property
    def id(self):
        return self._id
    
    @property
    def packages(self):
        return tuple(self._packages)
    
    @property
    def trucks(self):
        return tuple(self._trucks) 
    
    @property
    def locations(self):
        return self._locations
    
    # @locations.setter
    # def locations(self,value):
    #     self.ensure_locations_is_valid(value)
    #     self._locations.append(value)
    #     print(value)
    #     return self._locations

    def ensure_locations_is_valid(self,locations):
        if  (
            isinstance(locations, tuple) and 
            len(locations) == 2 and 
            isinstance(locations[0], (str, int)) and 
            isinstance(locations[1], datetime)
            ):
            return True
        raise ValueError('Invalid locations format')

    def calculate_route_distance(self):
        '''Depends on constants.distances when the matrix is ready'''
        pass

    def add_truck(self, truck):
        if truck not in self._trucks:
            return self._trucks.append(truck)
        pass

    def assign_package(self, package):
        if package not in self._packages:
            self._packages.append(package)
        else:
            raise ValueError("The package has been already assigned")

                
    def remove_package(self, pack_id):
        found_package = None
        for package in self._packages:
            if package.id == pack_id:
                found_package = package

        if package is None:
            return False
        else:
            self._packages.remove(found_package)
            return True    
            
   
       
    def __str__(self) -> str: 
        locations_and_times = []
        for location, time in self._locations:
            locations_and_times.append(f'{location} ({time})')
            
        return " -> ".join(locations_and_times)

    
    def info(self):
        info_str = f"Route ID: {self._id}\nLocations: {str(self)}\n"
        
        if self._packages:
            packages_str = "\nAssigned Packages:\n"
            for package in self._packages:
                packages_str += f"- Package ID: {package.id}, Start Location: {package.start_location}, End Location: {package.end_location}, Weight: {package.weight}kg\n"
            info_str += packages_str
        else:
            info_str += "\nNo packages assigned to this route.\n"
            
        if self._trucks:
            trucks_str = "\nTrucks:\n"
            for truck in self._trucks:
                trucks_str += f"- Truck ID: {truck.truck_id}, Name: {truck.name}, Capacity: {truck.capacity}kg, Max Range: {truck.max_range}km\n"
            info_str += trucks_str
        else:
            info_str += "\nNo trucks assigned to this route.\n"
        
        return info_str
    
    def get_expected_current_stop(self):
        current_time = datetime.now()
        for location, arrival_time in self._locations:
            if arrival_time > current_time:
                return location
        return self._locations[-1][0]
    
    
    def get_delivery_weight(self):
        assigned_weight = 0
        unassigned_weight = 0
        
        current_time = datetime.now()
        for location, time in self._locations[1:]:
            if time <= current_time:
                assigned_weight_at_stop = sum(package.weight for package in self._packages if package.start_location == location)
                unassigned_weight_at_stop = sum(package.weight for package in self._packages if package.end_location == location)
                assigned_weight += assigned_weight_at_stop
                unassigned_weight += unassigned_weight_at_stop

               
        delivery_weight = self._trucks[0].capacity + unassigned_weight - assigned_weight
        return delivery_weight
    
    
    
    
       
    
    
    