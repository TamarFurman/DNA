from commands.command_parser import parser_management
from commands.management.save import Save
from data_base.db import DB_sequences
from commands.management.delete import Delete
from data_base.dna_sequence import Dna_Sequence


class Management_Command:
    __instance = None
    creation_commands = {
        "del": Delete,
        "save": Save,
    }

    def __new__(cls, *args, **kwargs):
        if not Management_Command.__instance:
            Management_Command.__instance = object.__new__(cls)
        return Management_Command.__instance

    @staticmethod
    def execute(command):
        try:
            command_parser = parser_management(command)
        except Exception as err:
            return err
        sequence = Management_Command.creation_commands[command_parser[0]](command_parser[1], command_parser[2]).execute()
        if command_parser[0] == "del":
            if sequence == "cancel":
                print("action canceled.")
            else:
                print(f'Deleted: {sequence}')
                try:
                    DB_sequences.delete_sequence_by_id(sequence.get_id())
                except ValueError as value_err:
                    return value_err
                except KeyError as key_err:
                    return key_err
        elif isinstance(sequence,Dna_Sequence):
            print(f'Saved: {sequence}')
        else:
            print(sequence)

