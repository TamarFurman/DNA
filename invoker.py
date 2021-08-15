from commands.analysis.analysis_command import Analysis_Command
from commands.control_commands.list import List
from commands.control_commands.quit import Quit
from commands.creation.creation_command import Creation_Command
from commands.management.management_command import Management_Command
from commands.manipulation.manipulate_command import Manipulation


class Invoker:
    """
    This class is factory of all allowed command and their charge of running.
    """
    def __init__(self):
        self.command = ""
        from commands.batch.batch_command import Batch_Command
        self.commands = {
            "new": Creation_Command,
            "load": Creation_Command,
            "dup": Creation_Command,
            "slice": Manipulation,
            "replace": Manipulation,
            "contact": Manipulation,
            "pair": Manipulation,
            "del": Management_Command,
            "save": Management_Command,
            "len": Analysis_Command,
            "find": Analysis_Command,
            "count": Analysis_Command,
            "findall": Analysis_Command,
            "batch": Batch_Command,
            "run": Batch_Command,
            "batchlist": Batch_Command,
            "batchshow": Batch_Command,
            "batchsave": Batch_Command,
            "batchload": Batch_Command,
            "list": List(),
            "quit":Quit()
        }

    def get_command(self, command_name):
        """
        :param command_name: current command to run.
        :return:get it's responsible for parser and running.
        """
        if self.commands.get(command_name) is None:
            raise ValueError('not valid command')
        return self.commands[command_name]

    def run(self,command):
        """
        :param command: the command has to run.
        execute the command.
        """
        command_name = command.split()[0]
        self.get_command(command_name).execute(command)