from commands.batch.batch_creation import Batch_Creation
from commands.batch.batchlist import Batchlist
from commands.batch.batchload import Batchload
from commands.batch.batchsave import Batchsave
from commands.batch.batchshow import Batchshow
from commands.batch.run_batch import Run_Batch
from commands.command_parser import parser_creation, parser_batch


class Batch_Command:
    __instance = None
    creation_commands = {
        "batch": Batch_Creation,
        "run": Run_Batch,
        "batchlist":Batchlist,
        "batchshow": Batchshow,
        "batchsave": Batchsave,
        "batchload": Batchload,
    }

    def __new__(cls, *args, **kwargs):
        if not Batch_Command.__instance:
            Batch_Command.__instance = object.__new__(cls)
        return Batch_Command.__instance

    @staticmethod
    def execute(command):
        current_command = command.split()[0]
        try:
            if current_command == "batchsave" or current_command == "batchload":
                command_parser = parser_batch(command,"save")
            else:
                command_parser = parser_batch(command)
        except Exception as err:
            print(err)
            return
        if current_command == "batchsave" or current_command == "batchload":
            result = Batch_Command.creation_commands[command_parser[0]](command_parser[1],command_parser[2]).execute()
        else:
            result = Batch_Command.creation_commands[command_parser[0]](command_parser[1]).execute()
        if command_parser[0] == "batchlist" or command_parser[0] == "batchshow":
            print(result)
