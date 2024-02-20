from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.validation_helpers import validate_params_count


class CreateRoute(BaseCommand):
    def __init__(self, params: list[str],
                 app_data: ApplicationData,
                 models_factory: ModelsFactory):
        validate_params_count(params, 3, 'CreateRoute')
        super().__init__(params, app_data)
        self._models_factory = models_factory

    def execute(self):
        
        '''
        Encapsulates the logic for creating a new route  and adding it to the application data
        '''
        route_stops_str = self.params[0] #input format for route stops: MEL->SYD->BRI
        route_stops = route_stops_str.split("->")
        departure_time = self.params[1] + " " + self.params[2] #input format for time: YYYY-MM-DD HH:MM
        
        # estimate the arrival times for each route stop based on the departure time and route distances
        route_locations = self.app_data.get_estimated_arrival_times(route_stops, departure_time)
        route = self._models_factory.create_route(route_locations)
        self.app_data.add_route(route)

        return f'Route #{route._id} created'
