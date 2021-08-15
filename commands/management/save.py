from commands.command import Command
from data_base.db import DB_sequences
from data_base.dna_sequence import Dna_Sequence
from data_base.dna_status import DB_status


class Save(Command):
    def __init__(self, sequence, name):
        self.file_name = name
        super().__init__(name, sequence, None)
        self.confirm_delete = f"Do you really want to delete  {self.name}: {self.sequence}?" \
                              "Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'."

    def execute(self):
        try:
            seq = DB_sequences.get_seq(self.sequence)
            self.name = DB_sequences.get_name(self.sequence)
            self.id = DB_sequences.get_id(self.sequence)
            self.dna = Dna_Sequence(seq, self.name, self.id)
            if self.file_name == "None":
                self.file_name = f'{self.name}.rawdna'
            with open(self.file_name,'w+')as file:
                file.write(seq)
            try:
                DB_status.update_status(self.id,"up to date")
            except Exception as err:
                return err
            return self.dna
        except Exception as err:
            return err

    def __str__(self):
        return self.sequence.__str__()
