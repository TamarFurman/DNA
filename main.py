import re


def dna_sequence_appearance():
    # my_dna = Dna_Sequence("ACGTTTGCA")
    # first_len = len(my_dna)
    # before_insert = my_dna.get_dna_sequence()
    # my_dna.insert('T',1)
    # assert first_len != len(my_dna)
    # assert before_insert != my_dna.get_dna_sequence()
    # assert my_dna[0] == 'A'
    # assert my_dna == "ATCGTTTGCA"
    # assert my_dna != "ATC"
    # second_dna = Dna_Sequence("ATCGTTTGCA")
    # assert my_dna == second_dna
    # try:
    #     print(second_dna[11])
    # except IndexError:
    #     assert True
    my_dict = {"name":"tammy"}
    print(my_dict["car"])

if __name__ == '__main__':
    # dna_sequence_appearance()
    indexes = [m.start() for m in re.finditer('test', 'test test test test')]
    print(indexes)
