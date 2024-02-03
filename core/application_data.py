


class ApplicationData:
    def __init__(self):
        self.routes = []
        self.packages = []
        self.trucks = []

    def find_truck(self, truck_id):
        pass

    def find_route(self, start_location, end_location):
        pass

    def display_routes(self):
        pass

    def get_estimated_arrival_times(self, locations: list):
        pass

    def delivery_weight(self):
        pass

    def add_route(self, route):
        pass

    def add_package(self, package):
        pass

    def expected_current_stop(self, route, time_of_the_day):
        pass
    