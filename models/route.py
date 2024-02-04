from datetime import datetime, timedelta


class Route:
    def __init__(self, id, locations: list):
        self._id = id 
        self.packages = []
        self.trucks = []
        self.locations = [] #  [(location_1, departure_time), (location_2), arrival_time]

    def calculate_route_distance(self):
        pass

    def add_truck(self, truck):
        pass

    def add_package(self, package):
        pass
    
    def __str__(self) -> str:
        pass

    def display_route(self):
        pass