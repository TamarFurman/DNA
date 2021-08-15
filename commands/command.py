class Command:
    def __init__(self, name, sequence,dna):
        self.name = name
        self.sequence = sequence
        self.dna = dna

    def execute(self):
        raise Exception

    def __str__(self):
        raise Exception
