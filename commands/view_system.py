from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewSystem(BaseCommand):
    
    '''
    print information about all delivery routes in progress:
    it contains route ID, each route's stops, delivery weight, and the expected current stop based on the time of the day
    '''
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        super().__init__(params, app_data)
        

    def execute(self):
        all_routes_info = []
        if not self.app_data.routes:
            return 'Currently there are no routes in progress'
        
        for route in self.app_data.routes:
            delivery_weight = route.get_delivery_weight()
            expected_current_stop = route.get_expected_current_stop()
            route_info = (
                f'Route ID: {route._id}\n'
                f'{str(route)}\n'
                f'Delivery weight: {delivery_weight}\n'
                f'Expected current stop: {expected_current_stop}\n'
               )
            all_routes_info.append(route_info)
            
        return "\n".join(all_routes_info)
        