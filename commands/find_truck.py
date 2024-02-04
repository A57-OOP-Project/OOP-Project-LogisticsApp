from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.truck import Truck


class FindTruck(BaseCommand):
    '''
        finds a free truck that meets the required range and capacity
               
        '''
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        super().__init__(params, app_data)
        
        
    def execute(self):
       packages_weight = int(self.params[0])
       route_distance = int(self.params[1])

       # return 