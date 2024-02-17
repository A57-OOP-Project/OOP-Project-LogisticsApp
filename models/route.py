from datetime import datetime, timedelta
from models.package import Package
from models.truck import Truck
from commands.validation_helpers import try_parse_int

class Route:
    def __init__(self, id, locations: list):
        self._id = id 
        self._packages = []
        self._truck = None # For further implementation the application might include more than one truck per route
        self._locations = locations #  list of instances of class Location
          
         
    @property
    def truck(self):
        return self._truck

    @truck.setter
    def truck(self, value):
        self._truck = value    
        
    
    @property
    def id(self):
        return self._id
    
    @property
    def packages(self):
        return tuple(self._packages)
    
    
    @property
    def locations(self):
        return tuple(self._locations)   
   
    def get_expected_arrival_time(self, parcel_end_location):
        for location in self._locations:
            if location.city == parcel_end_location:
                return location.time.strftime('%Y-%m-%d %H:%M')
     
        
     
    def validate_locations(self, start_stop_of_parcel, end_stop_of_parcel): 
        start_index = None
        end_index = None                                       
        for index, location in enumerate(self._locations): 
            if location.city == start_stop_of_parcel:
                start_index = index
                
            elif location.city == end_stop_of_parcel:
                end_index = index
                break
                
        if start_index == None or end_index == None:                       
            return f'Route id #{self.route_id} is not suitable for the locations and direction of the package'
        
        return start_index, end_index
                                                                  
        
    def has_capacity(self, start_index, end_index, weight_of_parcel) -> bool: 
        '''                                                                                               
        Checks if the capacity of the truck in each location inside the given range from start_index to end_index
        will be enough for the weight ot the parcel.
        The method returns True if in all locations the truck has the required capacity 
        or False - if at least in one of the locations  thetruck  has not the required capacity
        '''     
        if self._packages:
            for idx in range(start_index, end_index):   
                if self.locations[idx].capacity < weight_of_parcel:
                  return False   
              
        return True           
                   
    
    def assign_package(self, package):
        if package not in self._packages:
            self._packages.append(package)
        else:
            raise ValueError("The package has been already assigned")

                
    def remove_package(self, pack_id):
        '''
        Remove package from the route.
        The method provides the opportunity to reassign packages, for example, in cases when an employee assigns wrong package to wrong route
        The possibility is not provided to remove packages from ApplicationData, list with packages.
        
        '''
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
        for location in self._locations:
            locations_and_times.append(f'{location.city} ({location.time.strftime('%Y-%m-%d %H:%M')})')
            
        return " -> ".join(locations_and_times)

    
    def info(self):
        info_str = f"Route ID: {self._id}\nLocations: {str(self)}"
        
        if self._packages:
            packages_str = "\nAssigned Packages:\n"
            for package in self._packages:
                packages_str += f"- Package ID: {package.id}, Start Location: {package.start_location}, End Location: {package.end_location}, Weight: {package.weight}kg\n"
            info_str += packages_str
        else:
            info_str += "\nNo packages assigned to this route.\n"
            
        if self._truck != None:
            truck_str = f"Truck ID: {self._truck.id}, Name: {self._truck.name}, Capacity: {self._truck.capacity}kg, Max Range: {self._truck.max_range}km\n"
            info_str += truck_str
        else:
            info_str += "\nNo trucks assigned to this route.\n"
        
        return info_str
    
    def get_expected_current_stop(self, time_delta):
        current_time = datetime.now() + timedelta(hours=time_delta)
        for location in self._locations:
            if location.time > current_time:
                return location.city
        return self._locations[-1].city
    
    
    def get_delivery_weight(self, time_delta): 
        current_time = datetime.now() + timedelta(hours=time_delta)
        delivery_weight = self.truck.capacity
        
        if current_time >= self.locations[0].time:
           for location in self.locations:
                if location.time <= current_time:
                    delivery_weight -= location.capacity
                else:
                    break  
        else:
            delivery_weight = 0  
        
        return delivery_weight
    
    
    
                   
    
    