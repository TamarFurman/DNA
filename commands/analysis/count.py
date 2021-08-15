from data_base.db import DB_sequences


class Count:
    def __init__(self, sequence1, sequence2):
        self.seq1 = sequence1
        self.seq2 = sequence2

    def execute(self):
        if all(c.upper() in 'ACGT' for c in self.seq2):
            seq2 = self.seq2
        else:
            try:
                seq2 = DB_sequences.get_seq(self.seq2)
            except Exception as err:
                return err
        try:
            seq1 = DB_sequences.get_seq(self.seq1)
        except Exception as err:
            return err
        return seq1.count(seq2)
