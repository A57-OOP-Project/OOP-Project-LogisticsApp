from datetime import datetime, timedelta


class Route:
    def __init__(self, id, locations: list):
        self._id = id 
        self.packages = []
        self.trucks = []
        self.locations = [] #  [(location_1, departure_time), (location_2), arrival_time)]

    
    def add_truck(self, truck):
        pass

    def assign_package(self, package):
        return self.packages.append(package)
        
    
    def __str__(self) -> str:
        pass

    def display_route(self):
        pass