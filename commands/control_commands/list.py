from data_base.db import DB_sequences
from data_base.dna_status import DB_status


class List:
    def __init__(self):
        self.sign_dict = {"up to date": "-", "modified": "*", "new": "o"}

    def execute(self, com):
        try:
            dna = DB_sequences.get_dna()
        except Exception as err:
            print(err)
            return
        for d in dna:
            try:
                status = DB_status.get_status(d.get_id())
            except Exception as err:
                print(err)
                return
            print(f'{self.sign_dict[status]} {d.__str__()}')
        return
