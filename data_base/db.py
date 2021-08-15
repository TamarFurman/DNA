import itertools
from data_base.dna_sequence import Dna_Sequence


class DB_sequences:
    DNA = dict()
    name_to_id = dict()
    __instance = None
    ids = itertools.count(start=1)

    def __new__(cls, *args, **kwargs):
        if not DB_sequences.__instance:
            DB_sequences.__instance = object.__new__(cls)
        return DB_sequences.__instance

    @staticmethod
    def add_sequence(sequence):
        if not isinstance(sequence, Dna_Sequence):
            return ValueError("excepted sequence value.")
        if sequence.get_id() in DB_sequences.DNA:
            return KeyError("sequence already exist.")
        DB_sequences.DNA[sequence.get_id()] = sequence
        DB_sequences.name_to_id[sequence.get_name()] = sequence.get_id()

    @staticmethod
    def delete_sequence_by_id(id):
        if not isinstance(id, int):
            return ValueError("excepted sequence value.")
        seq = DB_sequences.DNA.pop(id, None)
        item = DB_sequences.name_to_id.pop(DB_sequences.name_to_id.get(id))
        return KeyError("sequence not exist.") if seq or item is None else "ok"

    @staticmethod
    def get_sequence_by_id(id):
        sequence = DB_sequences.DNA.get(id, None)
        return KeyError("sequence not exist") if id is None else sequence

    @staticmethod
    def update_sequence(sequence):
        if not isinstance(sequence, Dna_Sequence):
            return ValueError("excepted sequence value.")
        if not sequence.get_id() in DB_sequences.DNA:
            return KeyError("sequence not exist.")
        DB_sequences.DNA[sequence.get_id()] = sequence
        DB_sequences.name_to_id[sequence.get_name()] = sequence.get_id()

    @staticmethod
    def delete_sequence_by_name(name):
        if not isinstance(name, str):
            return ValueError("excepted sequence value.")
        id = DB_sequences.DNA.pop(name, None)
        seq = DB_sequences.DNA.pop(id)
        return KeyError("sequence not exist.") if seq or id is None else "ok"

    @staticmethod
    def get_sequence_by_name(name):
        id = DB_sequences.name_to_id.get(name, None)
        return KeyError("sequence not exist") if id is None else DB_sequences.DNA.get(id)

    @staticmethod
    def get_name_of_id(id):
        val_index = list(DB_sequences.name_to_id.values()).index(id)
        return list(DB_sequences.name_to_id.keys())[val_index]

    @staticmethod
    def name_exist(name):
        return DB_sequences.name_to_id.get(name, None) is None

    @staticmethod
    def next_name(name, new=None, char=None):
        if char is None:
            char = ""
        without_name = itertools.count(start=1)
        if new is None:
            temp_name = name
        else:
            temp_name = f'{name}_{next(without_name)}'
        while not DB_sequences.name_exist(temp_name):
            temp_name = f'{name}_{char}{next(without_name)}'
        return temp_name

    @staticmethod
    def next_id():
        return next(DB_sequences.ids)

    @staticmethod
    def get_seq(seq):
        if seq.startswith("#"):
            return DB_sequences.get_sequence_by_id(int(seq[1:])).get_dna_sequence()
        if seq.startswith("@"):
            return DB_sequences.get_sequence_by_name(seq[1:]).get_dna_sequence()
        raise ValueError("The sequence has to start with # or @.")

    @staticmethod
    def get_name(seq):
        if seq.startswith("@"):
            return seq[1:]
        if seq.startswith("#"):
            return DB_sequences.get_name_of_id(int(seq[1:]))
        raise ValueError("The sequence has to start with # or @.")

    @staticmethod
    def get_id(seq):
        if seq.startswith("@"):
            return DB_sequences.name_to_id.get(seq[1:])
        if seq.startswith("#"):
            return int(seq[1:])
        raise ValueError("The sequence has to start with # or @.")

    @staticmethod
    def get_len(seq_id):
        try:
            id = int(seq_id)
        except ValueError:
            return "id has to be int."
        try:
            seq = DB_sequences.get_sequence_by_id(id).get_dna_sequence()
        except Exception as err:
            raise err
        return len(seq)

    @staticmethod
    def get_dna():
        return DB_sequences.DNA.values()