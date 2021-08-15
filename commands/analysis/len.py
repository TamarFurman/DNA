from data_base.db import DB_sequences


class Len:
    def __init__(self, sequence, name):
        self.sequence = sequence
        if name != "None":
            raise ValueError("arguments are not matches.")

    def execute(self):
        if not self.sequence.startswith("#"):
            return ValueError("id has to start with #.")
        try:
            seq_len = DB_sequences.get_len(self.sequence[1:])
            return seq_len
        except Exception as err:
            return err
