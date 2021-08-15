from data_base.dna_sequence import Dna_Sequence
from commands.command import Command
from data_base.db import DB_sequences


class Pair(Command):
    """
    Create sequence with its pair sequence, that is, each T is replaced by an A (and
    vice versa), and each C is replaced by a G (and vice versa).
    """
    def __init__(self, sequence, name):
        split_seq = sequence.split()
        if not len(split_seq) != 2:
            raise ValueError("arguments are not matches.")
        super().__init__(name, split_seq, None)
        self.swap = str.maketrans({'T': 'A', 'A': 'T', 'C': 'G', 'G': 'C', 't': 'a', 'a': 't', 'c': 'g', 'g': 'c'})

    def execute(self):
        """
        return dna's sequence or error if the action felt.
        """
        try:
            seq = DB_sequences.get_seq(self.sequence[0])
            temp_name = DB_sequences.get_name(self.sequence[0])
            id = DB_sequences.get_id(self.sequence[0])
            self.sequence = seq.translate(self.swap)
            if self.name == "None":
                self.name = temp_name
            else:
                if self.name.startswith(" "):
                    self.name = self.name[1:]
                self.name = DB_sequences.next_name(temp_name, None,
                                                   'p') if self.name == "@@" else DB_sequences.next_name(self.name[1:],
                                                                                                         None, 'p')
                id = DB_sequences.next_id()
            self.dna = Dna_Sequence(self.sequence, self.name, id)
            return self.dna
        except Exception as err:
            return err

    def __str__(self):
        return self.sequence.__str__()
