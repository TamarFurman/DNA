from commands.creation.new import New
from commands.creation.load import Load
from commands.creation.dup import Dup
from commands.command_parser import parser_creation
from data_base.db import DB_sequences


class Creation_Command:
    """
    The following commands are being used to generate new sequences.
    The design pattern is factory and singleton.
    """
    __instance = None
    creation_commands = {
        "new": New,
        "load": Load,
        "dup": Dup
    }

    def __new__(cls, *args, **kwargs):
        if not Creation_Command.__instance:
            Creation_Command.__instance = object.__new__(cls)
        return Creation_Command.__instance

    @staticmethod
    def execute(command):
        """
        :param command: current command to run.
        call to parser of this group command and execute the command.
        print the result of executing.
        create a new dna.
        """
        try:
            command_parser = parser_creation(command)
        except Exception as err:
            return err
        sequence = Creation_Command.creation_commands[command_parser[0]](command_parser[1], command_parser[2]).execute()
        print(sequence)
        try:
            DB_sequences.add_sequence(sequence)
        except ValueError as value_err:
            return value_err
        except KeyError as key_err:
            return key_err