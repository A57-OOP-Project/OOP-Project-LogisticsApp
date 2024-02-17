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
        
        input_line = 'asd 1 2 3'
        cmd_factory, app_data = test_setup()
        
        with self.assertRaises(InvalidCommand):
            command = cmd_factory.create(input_line)
        
        
    def test_createPackageCommand_withCorrectParams(self):
       
        input_line = 'createpackage MEL SYD 1000 BaiGanio,phone:0888123444'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, CreatePackage)
        self.assertIsInstance(command._models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('MEL', 'SYD', '1000', 'BaiGanio,phone:0888123444'), command.params)
        
    def test_createRouteCommand_withCorrectParams(self):
       
        input_line = 'createroute MEL->SYD->BRI 2024-02-18 14:30'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, CreateRoute)
        self.assertIsInstance(command._models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('MEL->SYD->BRI', '2024-02-18', '14:30'), command.params)
        
    def test_createViewNotAssignedCommand_withCorrectParams(self):
       
        input_line = 'viewnotassigned'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, ViewNotAssigned)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual((), command.params)
        
    def test_createAddPackageCommand_withCorrectParams(self):
       
        input_line = 'addpackage 1 1'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, AddPackage)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('1', '1'), command.params)
        
        
    def test_createViewPackageCommand_withCorrectParams(self):
       
        input_line = 'viewpackage 1'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, ViewPackage)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('1',), command.params)
        
        
    def test_createAddTruckCommand_withCorrectParams(self):
       
        input_line = 'addtruck scania 1001 1'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, AddTruck)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('scania', '1001', '1'), command.params)
        
        
    def test_createViewRouteCommand_withCorrectParams(self):
       
        input_line = 'viewroute 1'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, ViewRoute)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('1',), command.params)
        
    def test_createFindRouteCommand_withCorrectParams(self):
       
        input_line = 'findroute ASP MEL'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, FindRoute)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('ASP', 'MEL'), command.params)
        
    def test_createCheckRouteCapacityCommand_withCorrectParams(self):
       
        input_line = 'checkroutecapacity 1 MEL SYD 1000'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, CheckRouteCapacity)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('1', 'MEL', 'SYD', '1000'), command.params)
        
    def test_createRemovePackageFromRouteCommand_withCorrectParams(self):
       
        input_line = 'removepackagefromroute 1 1'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, RemovePackageFromRoute)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('1', '1'), command.params)
        
    def test_createFindTruckCommand_withCorrectParams(self):
       
        input_line = 'findtruck 1000 MEL SYD BRI'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, FindTruck)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('1000', 'MEL', 'SYD', 'BRI'), command.params)
        
    def test_createViewSystemCommand_withCorrectParams(self):
       
        input_line = 'viewsystem 0'
        cmd_factory, app_data = test_setup()

        command = cmd_factory.create(input_line)

        self.assertIsInstance(command, ViewSystem)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(('0',), command.params)
        
    
      
        
    
        
        
    
    
        
    
        
        
        
    
        
        
        
        
        
        
    
    

    
