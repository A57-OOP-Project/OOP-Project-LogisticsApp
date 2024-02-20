from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.validation_helpers import validate_params_count, try_parse_int


class CreatePackage(BaseCommand): 
    def __init__(self, params: list[str],
                 app_data: ApplicationData,
                 models_factory: ModelsFactory):
        validate_params_count(params, 4, 'CreatePackage')
        super().__init__(params, app_data)
        self._models_factory = models_factory

    def execute(self):
        '''
         Encapsulates the logic for creating a new package by utilizing the ModelsFactory to instantiate the Package class
         and adding the created package to the application data
        
        '''
        start_location, end_location, weight_str, contact_info = self.params
        weight = try_parse_int(
            weight_str, 'Weight should be an integer number')
        #creates an instance of class Package
        package = self._models_factory.create_package(start_location, end_location, weight, contact_info)
        self.app_data.add_package(package)

        return f'Package #{package._id} created'


       
 
 
 
 
  