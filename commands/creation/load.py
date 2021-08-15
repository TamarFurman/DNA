from data_base.dna_sequence import Dna_Sequence
from commands.command import Command
from data_base.db import DB_sequences
import os

from data_base.dna_status import DB_status


class Load(Command):
    """
    loads the sequence from the file and assigns it.
    """
    def __init__(self, sequence, name):
        super().__init__(name, sequence, None)

    def execute(self):
        """
        return dna's sequence or error if the action felt.
        """
        if self.name == "None":
            self.name = DB_sequences.next_name(self.sequence.split(".")[0])
        else:
            if not self.name.startswith("@"):
                return ValueError("name has to start with @.")
        if not "." in self.sequence:
            self.sequence = self.sequence + ".rawdna"
        if os.path.exists(f'./{self.sequence}'):
            with open(self.sequence, "r") as file:
                self.sequence = file.readlines()[0]
        else:
            raise ValueError("file not found")
        id = DB_sequences.next_id()
        self.dna = Dna_Sequence(self.sequence, self.name, id)
        try:
            DB_status.add_dna(id, "up to date")
        except Exception as err:
            return err
        return self.dna

    def __str__(self):
        return self.sequence.__str__()
