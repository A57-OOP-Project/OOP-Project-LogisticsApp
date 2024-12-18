#from __future__ import annotations
from models.constants.distances import Distances
from datetime import datetime, timedelta
from models.package import Package
from models.route import Route
from models.truck import Truck
from models.constants.truck_types import TruckTypes
from models.location import Location
import pickle
import os 
from models.schedule import Schedule

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

        
    def find_package_by_id(self, pack_id: int) -> Package:
        for package in self._packages:
            if package._id == pack_id:
                return package
        
        raise ValueError(f'Invalid package id: {pack_id}')    
            

    
    def find_route_by_id(self, r_id: int) -> Route:
        found_route = None
        for route in self._routes:
            if route._id == r_id:
                found_route = route
        if found_route == None:
            raise ValueError(f'Invalid route id #{r_id}')
        
        return found_route
    
            
    def is_truck_assigned(self, id: int) -> bool:
        return id in [truck._id for truck in self._trucks]
    
    
    def find_truck_by_id(self, tr_id: int) -> Truck:
        
        for truck in self._trucks:
            if truck.id == tr_id:
                return truck
            
        raise ValueError(f'Invalid truck id: {tr_id}')    
        
    
        
    def get_estimated_arrival_times(self, locations_strings: list[str], departure_time: str): #departure_time is a string in format 'YYYY-MM-DD HH:MM'
        '''
        Calculates the estimated arrival times for a list of locations based on the departure time and the distances 
        between consecutive locations.
        Parameters:
           locations_strings: A list of strings representing the names of the locations to be visited in order
           departure_time: A string representing the departure time in the format 'YYYY-MM-DD HH:MM'
           
        It returns the list of Location objects representing each location in the route,along with their estimated arrival times
        '''  
        try:
            departure_datetime = datetime.strptime(departure_time, '%Y-%m-%d %H:%M')
        except ValueError:
            raise ValueError("Invalid format for departure time. Please use 'YYYY-MM-DD HH:MM'")

        
        locations = []
        start_location = Location(locations_strings[0], departure_datetime)
        locations.append(start_location)
        
        for i in range(1, len(locations_strings)):
            current_time = locations[-1].time
            location = locations_strings[i]
            travel_time = Distances.calculate_distance(locations_strings[i-1:i+1]) / 87  #average speed is 87 km/h
            arrival_time = current_time + timedelta(hours=travel_time)
            location_of_the_route = Location(location, arrival_time)
            locations.append(location_of_the_route)
            
        return locations
     
        
    def find_suitable_trucks(self, packages_weight: int, route_distance: int):
        '''
         Finds trucks that are suitable for carrying a given package based on the package's weight and 
         the distance of the route it needs to travel. 
         Parameters:
            packages_weight
            route_distance
             
        Return Values:
           suitable_available_trucks: IDs of available trucks suitable for carrying the package
           suitable_involved_trucks: Information about routes involving trucks that are suitable for carrying the package
           unsuitable_trucks: Set of truck types that are unsuitable for carrying the package
        '''
        suitable_available_trucks = []
        suitable_involved_trucks = []
        unsuitable_trucks = set()
        
        for truck_type, truck_info in TruckTypes.DATA.items():
            if truck_info['capacity'] >= packages_weight and truck_info['max_range'] >= route_distance:
                truck_ids = range(truck_info['ids_min'], truck_info['ids_max'] + 1)
                for truck_id in truck_ids:
                    if not self.is_truck_assigned(truck_id):
                        suitable_available_trucks.append(truck_id)
                    else:
                        for route_id in Schedule.DATA[truck_id]:
                            route = self.find_route_by_id(route_id)
                            suitable_involved_trucks.append(f'Route id #{route_id}: {str(route)}')
            else: unsuitable_trucks.add(truck_type)
             
        return suitable_available_trucks, suitable_involved_trucks, unsuitable_trucks
    
  
    def is_schedule_conflict(self, truck_id: int, route_id_number: int) -> bool:
        '''
        Checks if there's a scheduling conflict between a new route and existing routes assigned to a particular truck.
        Parameters:
           truck_id: ID of the truck for which the conflict needs to be checked
           route_id_number: ID of the new route
        If it finds any overlap between the time boundaries of the new route and any existing route,
        it returns True, indicating a scheduling conflict. Otherwise, if no conflict is found, it returns False.  
        '''
        new_route = self.find_route_by_id(route_id_number) 
        start_time_new_route = new_route.locations[0].time
        end_time_new_route = new_route.locations[-1].time
            
        for route_id in Schedule.DATA[truck_id]:
           route_in_schedule = self.find_route_by_id(route_id)
           start_time_route_in_schedule = route_in_schedule.locations[0].time
           end_time_route_in_schedule = route_in_schedule.locations[-1].time
           if start_time_route_in_schedule <= end_time_new_route and end_time_route_in_schedule >= start_time_new_route:
               return True
           
        return False
       
       
    def save_data(self):
        '''
        this method is responsible for saving the application data to a file using the pickle module
        
        '''
        data = {
            "routes": self._routes,
            "packages": self._packages,
            "trucks": self._trucks,
        }
 
        file_path = "data/app_data.pickle"
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
 
        with open("data/app_data.pickle", "wb") as file:
            pickle.dump(data, file)
 
    def load_data(self):
        '''
        this  method is responsible for loading the application data from the saved file
        
        '''
        if os.path.isfile("data/app_data.pickle"):
            with open("data/app_data.pickle", "rb") as file:
                data = pickle.load(file)
                self._routes = data["routes"]
                self._packages = data["packages"]
                self._trucks = data["trucks"]