from models.constants.distances import Distances
from datetime import datetime, timedelta


class ApplicationData:
    def __init__(self):
        self.routes = []
        self.packages = []
        self.trucks = []

    def add_truck(self, packages_weight, route_distance):
        
        pass

    def find_route(self, route_id):
        pass

    def find_package(self, package_id):
        pass

    def display_routes(self):
        pass

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
        
       

        #return lst_locations

    def get_delivery_weight(self):
        pass

    def add_route(self, route):
        pass

    def add_package(self, package):
        pass

    def get_expected_current_stop(self, route, time_of_the_day):
        pass
    