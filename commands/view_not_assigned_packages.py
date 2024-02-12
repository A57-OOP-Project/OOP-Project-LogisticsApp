from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData



class ViewNotAssigned(BaseCommand):
    
    '''
    print info about each package that is not yet assigned to a delivery route:
    list of packages containing their IDs and locations
    '''
    def __init__(self, params: list[str],
                 app_data: ApplicationData):
        super().__init__(params, app_data)
        

    def execute(self):
        unassigned_info = []
        
        for package in self.app_data.packages:
            is_assigned = False
            for route in self.app_data.routes:
                if package in route.packages:
                    is_assigned = True
                    break
            if not is_assigned:
                unassigned_info.append(package.info())
                 
        return  "\n".join(unassigned_info)
        