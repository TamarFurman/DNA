from data_base.dna_sequence import Dna_Sequence
from commands.command import Command
from data_base.db import DB_sequences


class Slice(Command):
    """
    Slices the sequence, so that starts in first index was given and ends in second index.
    (inclusive)
    """
    def __init__(self, sequence, name):
        split = sequence.split()
        if len(split) != 3:
            raise ValueError("arguments are not matches.")
        super().__init__(name, split, None)

    def execute(self):
        """
        return dna's sequence or error if the action felt.
        """
        try:
            seq = DB_sequences.get_seq(self.sequence[0])
            temp_name = DB_sequences.get_name(self.sequence[0])
            id = DB_sequences.get_id(self.sequence[0])
            self.sequence = seq[int(self.sequence[1]):int(self.sequence[2])]
            if self.name == "None":
                self.name = temp_name
            else:
                if self.name.startswith(" "):
                    self.name = self.name[1:]
                self.name = DB_sequences.next_name(temp_name,None,'s') if self.name == "@@" else DB_sequences.next_name(self.name[1:],None,'s')
                id = DB_sequences.next_id()
            self.dna = Dna_Sequence(self.sequence, self.name, id)
            return self.dna
        except Exception as err:
            return err


    def __str__(self):
        return self.sequence.__str__()
