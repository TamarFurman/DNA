from data_base.dna_sequence import Dna_Sequence
from commands.command import Command
from data_base.db import DB_sequences


class Replace(Command):
    """
    replaces the letter in the 2 indexes were given.
    """
    def __init__(self, sequence, name):
        split_seq = sequence.split()
        if not (len(split_seq)>0 and len(split_seq)%2 == 1):
            raise ValueError("arguments are not matches.")
        super().__init__(name, split_seq, None)

    def execute(self):
        """
        return dna's sequence or error if the action felt.
        """
        try:
            seq = DB_sequences.get_seq(self.sequence[0])
            temp_name = DB_sequences.get_name(self.sequence[0])
            id = DB_sequences.get_id(self.sequence[0])
            seq = list(seq)
            for i in range(1,len(self.sequence)-1,2):
                seq[int(self.sequence[i])-1] = self.sequence[i+1]
            self.sequence = "".join(seq)
            if self.name == "None":
                self.name = temp_name
            else:
                if self.name.startswith(" "):
                    self.name = self.name[1:]
                self.name = DB_sequences.next_name(temp_name,None) if self.name == "@@" else DB_sequences.next_name(self.name[1:],None)
                id = DB_sequences.next_id()
            self.dna = Dna_Sequence(self.sequence, self.name, id)
            return self.dna
        except Exception as err:
            return err


    def __str__(self):
        return self.sequence.__str__()
