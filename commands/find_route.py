from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from datetime import datetime
from models.route import Route
from commands.validation_helpers import validate_params_count


class FindRoute(BaseCommand):
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        validate_params_count(params, 2, 'FindRoute')
        super().__init__(params, app_data)
        
    # Search for a route based on package’s start and end locations    
    def execute(self):
        start_location, end_location = self.params
        current_time = datetime.now()
        routes = []
        start_point_time = None
        end_point_time = None
        for route in self.app_data.routes:
            for location, time in route.locations:
                if location == start_location and time >= current_time:
                    start_point_time = time
                if location == end_location and time >= current_time:
                    end_point_time = time 
        if start_point_time == None or end_point_time == None:
            return f'There are not suitable routes in progress for the specified parameters'
        if start_point_time < end_point_time:
            routes.append(f'Route id #{route._id}:' + str(route))
        
        return "\n".join(routes)
    
    