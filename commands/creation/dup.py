from data_base.dna_sequence import Dna_Sequence
from data_base.db import DB_sequences
from commands.command import Command
from data_base.dna_status import DB_status


class Dup(Command):
    """
    duplicates the sequence.
    """
    def __init__(self, sequence, name):
        super().__init__(name,sequence, None)

    def execute(self):
        """
        return dna's sequence or error if the action felt.
        """
        try:
            seq= DB_sequences.get_seq(self.sequence)
            temp_name = DB_sequences.get_name(self.sequence)
            if self.name == "None":
                self.name = temp_name
            else:
                if self.name.startswith("@"):
                    self.name = self.name[1:]
                else:
                    return ValueError("name has to start with @.")
            self.name = DB_sequences.next_name(self.name)
            id = DB_sequences.next_id()
            self.dna = Dna_Sequence(seq, self.name, id)
            try:
                DB_status.add_dna(id)
            except Exception as err:
                return err
            return self.dna
        except Exception as err:
            return err

    def __str__(self):
        return self.dna.__str__()
