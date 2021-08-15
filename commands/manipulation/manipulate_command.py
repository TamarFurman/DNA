from commands.manipulation.contact import Contact
from commands.manipulation.pair import Pair
from commands.manipulation.slice import Slice
from commands.manipulation.replace import Replace
from commands.command_parser import parser_manipulation
from data_base.db import DB_sequences
from data_base.dna_status import DB_status


class Manipulation:
    """
    This is class that hold Manipulation group commands.
    The following commands manipulate existing sequences.
    The design pattern is factory and singleton.
    """
    __instance = None
    manipulation_commands = {
        "slice": Slice,
        "replace": Replace,
        "contact": Contact,
        "pair": Pair,
    }

    def __new__(cls, *args, **kwargs):
        if not Manipulation.__instance:
            Manipulation.__instance = object.__new__(cls)
        return Manipulation.__instance

    @staticmethod
    def execute(command):
        """
        :param command: current command to run.
        call to parser of this group command and execute the command.
        print the result of executing.
        create a new dna or modified current dna according to the input.
        """
        try:
            command_parser = parser_manipulation(command)
        except Exception as err:
            return err
        sequence = Manipulation.manipulation_commands[command_parser[0]](command_parser[1], command_parser[2]).execute()
        print(sequence)
        if command_parser[-1] == "None":
            try:
                DB_sequences.update_sequence(sequence)
                DB_status.update_status(sequence.get_id())
            except ValueError as value_err:
                return value_err
            except KeyError as key_err:
                return key_err
        else:
            try:
                DB_sequences.add_sequence(sequence)
                DB_status.add_dna(sequence.get_id())
            except ValueError as value_err:
                return value_err
            except KeyError as key_err:
                return key_err

