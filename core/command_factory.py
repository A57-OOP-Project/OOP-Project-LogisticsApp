from commands.view_system import ViewSystemCommand
from core.application_data import ApplicationData
from commands.add_package import AddPackage
from commands.add_route import AddRoute
from commands.find_route import FindRoute
from commands.view_system import ViewSystem
from core.models_factory import ModelsFactory

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data
        self._models_factory = ModelsFactory()

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "addpackage":
            return AddPackage(params, self._app_data, self._models_factory)
        if cmd.lower() == "addroute":
            return AddRoute(params, self._app_data, self._models_factory)
        if cmd.lower() == "findroute":
            return FindRoute(params, self._app_data)
        if cmd.lower() == "viewsystem":
            return ViewSystem(params, self._app_data)
        
        raise ValueError(f'Invalid command name: {cmd}!')
