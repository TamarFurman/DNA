from commands.command import Command
from data_base.db import DB_sequences
from data_base.dna_sequence import Dna_Sequence


class Delete(Command):
    def __init__(self, sequence, name):
        super().__init__(name, sequence, None)

    def execute(self):
        try:
            seq = DB_sequences.get_seq(self.sequence)
            self.name = DB_sequences.get_name(self.sequence)
            self.id = DB_sequences.get_id(self.sequence)
            self.dna = Dna_Sequence(seq, self.name, self.id)
            user_input = ''
            print(self.confirm_delete())
            while user_input.upper() not in ['Y','N']:
                user_input = input("> confirm >>>")
                if user_input.upper() not in ['Y','N']:
                    print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
            if user_input.upper() == 'Y':
                return self.dna
            return "cancel"
        except Exception as err:
            return err

    def confirm_delete(self):
        return f"Do you really want to delete  {self.name}: {self.sequence}?\n" \
               f"Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'."

    def __str__(self):
        return self.sequence.__str__()
