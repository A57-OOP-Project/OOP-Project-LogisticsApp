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
        return tuple(self._locations)   
   
    def get_expected_arrival_time(self, parcel_end_location):
        for location, time in self._locations:
            if location == parcel_end_location:
                return time
    
    
    def update(self):
        '''
        Currently updates info about parcels assigned to a given route and capacity of the truck.
        '''
        assigned_weight = 0
        unassigned_weight = 0
        unassigned_packages = []
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")   
        current_location = self._locations[0][0]
        for location, time in self._locations:
            if time <= current_time:
                current_location = location
                
        for package in self._packages:
            if package.end_location == current_location:
                unassigned_weight += package.weight
                unassigned_packages.append(package._id)
            if package.start_location == current_location:
                assigned_weight += package.weight
        
        self._trucks[0].capacity = self._trucks[0].capacity + unassigned_weight - assigned_weight
        self._packages = [package for package in self._packages if package._id not in unassigned_packages] 
                                                                  
        
    def check_capacity(self, start_location_of_parcel, end_location_of_parcel, weight_of_parcel):
        '''
        Calculates capacity that the truck will have in each location along the route of a given parcel.
        The method returns True if in all locations the truck will have the required capacity 
        or False - if at least in one of the locations along the route of this parcel the truck will not have the required capacity
        '''
       
        current_capacity = self._trucks[0].capacity # for simplicity, let's assume that there is only one truck assigned to each route 
        unassigned_packages = 0 
        assigned_packages  = 0
                                      
        for index, (location, _) in enumerate(self._locations):
            if location == start_location_of_parcel:
                start_index = index
            if location == end_location_of_parcel:
                end_index = index
        if self._packages:
            for idx in range(start_index, end_index):   
               unassigned_packages = sum(package.weight for package in self._packages if package.end_location == self._locations[idx][0])
               assigned_packages = sum(package.weight for package in self._packages if package.start_location == self._locations[idx][0])
        
        capacity = current_capacity + unassigned_packages - assigned_packages 
        if capacity < weight_of_parcel:
            return False   
    
        return True                   
                   

    
    def assign_truck(self, truck):
            self._trucks.append(truck) # for simplicity, let's assume that there is only one truck assigned to each route

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
    
    
    
    
       
    
    
    