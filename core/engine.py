from core.command_factory import CommandFactory

""" class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output = []
        while True:
            try:
                input_line = input("Enter command, please: ")
                if input_line.lower() == 'end':
                    break

                command = self._command_factory.create(input_line)
                output.append(command.execute())
            except Exception as err:
                output.append(err.args[0])

        print('\n'.join(output)) """


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output = []
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'end':
                    break

                command = self._command_factory.create(input_line)
                output.append(command.execute())
            except Exception as err:
                output.append(err.args[0])

        print('\n'.join(output)) 