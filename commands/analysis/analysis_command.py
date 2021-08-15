from commands.analysis.count import Count
from commands.analysis.find import Find
from commands.analysis.findall import Findall
from commands.analysis.len import Len
from commands.command_parser import parser_creation


class Analysis_Command:
    __instance = None
    creation_commands = {
        "len": Len,
        "find": Find,
        "count": Count,
        "findall": Findall
    }

    def __new__(cls, *args, **kwargs):
        if not Analysis_Command.__instance:
            Analysis_Command.__instance = object.__new__(cls)
        return Analysis_Command.__instance

    @staticmethod
    def execute(command):
        try:
            command_parser = parser_creation(command)
        except Exception as err:
            return err
        sequence = Analysis_Command.creation_commands[command_parser[0]](command_parser[1], command_parser[2]).execute()
        print(sequence)
