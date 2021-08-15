from data_base.dna_sequence import Dna_Sequence
from commands.command import Command
from data_base.db import DB_sequences


class Contact(Command):
    """
    Concatenation of dnas' sequences.
    """
    def __init__(self, sequence, name):
        split_seq = sequence.split()
        if not len(split_seq) > 1:
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
            new_name = temp_name
            for i in range(1,len(self.sequence)):
                seq += DB_sequences.get_seq(self.sequence[i])
                new_name = new_name+"_"+DB_sequences.get_name(self.sequence[i])
            if self.name == "None":
                self.name = temp_name
            else:
                if self.name.startswith(" "):
                    self.name = self.name[1:]
                self.name = DB_sequences.next_name(new_name,None,'c') if self.name == "@@" else DB_sequences.next_name(self.name[1:],None,'c')
                if len(self.sequence) >= 3:
                    self.name = DB_sequences.next_name("conseq")
                id = DB_sequences.next_id()
            self.sequence = seq
            self.dna = Dna_Sequence(self.sequence, self.name, id)
            return self.dna
        except Exception as err:
            return err

    def __str__(self):
        return self.sequence.__str__()
