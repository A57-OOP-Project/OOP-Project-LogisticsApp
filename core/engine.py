from core.command_factory import CommandFactory

class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory
        self.app_data = self._command_factory.get_app_data()
        
    def start(self):
        self.app_data.load_data() #Load data from file if it exists
        
        
        while True:
            output = ''
            try:
                input_line = input("Please enter your command: ")
                if input_line.lower() == 'end':
                    break

                command = self._command_factory.create(input_line)
                output = command.execute()
            except Exception as err:
                output = err.args[0]
            print(output)   
              
        self.app_data.save_data()

        #print('\n'.join(output)) 


# class Engine:
#     def __init__(self, factory: CommandFactory):
#         self._command_factory = factory

#     def start(self):
#         output = []
#         while True:
#             try:
#                 input_line = input()
#                 if input_line.lower() == 'end':
#                     break

#                 command = self._command_factory.create(input_line)
#                 output.append(command.execute())
#             except Exception as err:
#                 output.append(err.args[0])

#         print('\n'.join(output)) 