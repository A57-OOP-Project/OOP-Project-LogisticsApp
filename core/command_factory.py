from commands.view_system import ViewSystem
from core.application_data import ApplicationData
from commands.add_packages import AddPackages
from commands.add_truck import AddTruck
from commands.find_route import FindRoute
from commands.view_system import ViewSystem
from core.models_factory import ModelsFactory
from commands.find_truck import FindTruck
from commands.create_package import CreatePackage
from commands.create_route import CreateRoute
from commands.view_not_assigned_packages import ViewNotAssigned
from commands.view_package_info import ViewPackage
from commands.remove_package import RemovePackageFromRoute
from commands.check_route import CheckRouteCapacity
from errors.invalid_command import InvalidCommand

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data
        self._models_factory = ModelsFactory()

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "createpackage":
            return CreatePackage(params, self._app_data, self._models_factory)
        if cmd.lower() == "createroute":
            return CreateRoute(params, self._app_data, self._models_factory)
        if cmd.lower() == "addpackages":
            return AddPackages(params, self._app_data)
        if cmd.lower() == "addtruck":
            return AddTruck(params, self._app_data)
        if cmd.lower() == "findroute":
            return FindRoute(params, self._app_data)
        if cmd.lower() == "checkroutecapacity":
            return CheckRouteCapacity(params, self._app_data)
        if cmd.lower() == "removepackagefromroute":
            return RemovePackageFromRoute(params, self._app_data)
        if cmd.lower() == "findtruck":
            return FindTruck(params, self._app_data)
        if cmd.lower() == "viewsystem":
            return ViewSystem(params, self._app_data)
        if cmd.lower() == "viewnotassigned":
            return ViewNotAssigned(params, self._app_data)
        if cmd.lower() == "viewpackage":
            return ViewPackage(params, self._app_data)
        
        raise InvalidCommand(cmd)
