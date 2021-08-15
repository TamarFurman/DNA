from commands.command import Command
from data_base.db import DB_sequences
from data_base.dna_sequence import Dna_Sequence
from data_base.dna_status import DB_status


class New(Command):
    """
    Creates a new sequence.
    """
    def __init__(self, sequence, name):
        super().__init__(name, sequence, None)

    def execute(self):
        """
        return dna's sequence or error if the action felt.
        """
        if self.name == "None":
            self.name = "@" + DB_sequences.next_name('seq', 'new')
        elif not self.name.startswith("@"):
            raise ValueError("The name of the sequence has to start with @.")
        id = DB_sequences.next_id()
        self.dna = Dna_Sequence(self.sequence, self.name[1:], id)
        try:
            DB_status.add_dna(id)
        except Exception as err:
            return err
        return self.dna

    def __str__(self):
        return self.sequence.__str__()
