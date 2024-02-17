from commands.view_system import ViewSystem
from core.application_data import ApplicationData
from commands.add_package import AddPackage
from commands.add_truck import AddTruck
from commands.find_route import FindRoute
from commands.view_system import ViewSystem
from core.models_factory import ModelsFactory
from commands.find_truck import FindTruck
from commands.create_package import CreatePackage
from commands.create_route import CreateRoute
from commands.view_not_assigned_packages import ViewNotAssigned
from commands.view_package import ViewPackage
from commands.remove_package import RemovePackageFromRoute
from commands.check_route import CheckRouteCapacity
from errors.invalid_command import InvalidCommand
from commands.view_route import ViewRoute
from core.command_factory import CommandFactory
from unittest import TestCase

def test_setup():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    return cmd_factory, app_data

class Create_Should(TestCase):
    
    def test_raiseError_invalidCommandName(self):
        # Arrange
        input_line = 'asd 1 2 3'
        cmd_factory, app_data = test_setup()

        #to be continued :)
