from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory


class AddPackage(BaseCommand):
    def __init__(self, params: list[str],
                 app_data: ApplicationData,
                 models_factory: ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory

    def execute(self):
        pass

       # return f'Package #{package_id} created'
