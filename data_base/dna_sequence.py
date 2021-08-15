import re


class Dna_Sequence:
    """
    class of DNA Sequence
    """

    def __init__(self, dna_string, name, id):
        """
        initialization the dna string ,name and id.
        :param dna_string: sequence of dna nucleotide.
        :param name: name of the dna sequence.
        :param id: id of the dna sequence.
        """
        self.set_dna_sequence(dna_string)
        self.set_name(name)
        self.set_id(id)

    def get_dna_sequence(self):
        """
        :return: the dna sequence of the object.
        """
        return self.__dna_sequence

    def set_dna_sequence(self, string):
        """
        initialization a dnaSequence object if not valid ValueError would be raised.
        :param string: a dna sequence that should be replace the current sequence.
        """
        if not all(c.upper() in 'ACGT' for c in string):
            raise ValueError("not all the string composed of nucleotide")
        self.__dna_sequence = string

    def get_name(self):
        """
        :return: the name of  the sequence object.
        """
        return self.__name

    def set_name(self, name):
        """
        initialization the name of the object if not valid ValueError would be raised.
        :param name:  a name of  sequence that should be replace the current name.
        """
        if not isinstance(name, str):
            raise ValueError("name has to be string")
        self.__name = name

    def get_id(self):
        """
        :return: the id of the sequence object.
        """
        return self.__id

    def set_id(self, id):
        """
        initialization the id of the object if not valid ValueError would be raised.
        :param name:  a name of sequence that should be replace the current name.
        """
        if not isinstance(id, int):
            raise ValueError("name has to be string")
        self.__id = id

    def insert(self, nucleotide, index):
        """
        :param nucleotide: a single nucleotide,if not valid ValueError would be raised.
        :param index: specifies index in ordrf to insert the nucleotide into the dna sequence.
        :return: nothing would be returned.
        """
        if index >= len(self.__dna_sequence):
            raise IndexError
        elif nucleotide.upper() not in "AGCT":
            raise ValueError
        self.set_dna_sequence(self.get_dna_sequence()[:index] + nucleotide + self.get_dna_sequence()[index:])

    def __str__(self):
        """
        :return: format of the dna sequence.
        """
        if len(self.get_dna_sequence()) <= 40:
            return f'[{self.get_id()}] {self.get_name()}:{self.__dna_sequence}'
        return f'[{self.get_id()}] {self.get_name()}:{self.__dna_sequence[:33]+"..."+self.__dna_sequence[-3:]}'

    def __eq__(self, other):
        """
        operator overloading of equals function.
        :param other:another object to compare to.
        :return:bool- True if the objects are equals,otherwise False.
        """
        if hasattr(other, 'get_dna_sequence'):
            return self.__dna_sequence == other.get_dna_sequence()
        elif isinstance(other, str):
            return self.get_dna_sequence() == other

    def __ne__(self, other):
        """
        operator overloading of non equals function.
        :param other: another object to compare to.
        :return: bool- True if the objects aren't equals,otherwise False.
        """
        return not self == other

    def __getitem__(self, index):
        """
        :param index:an index if not exist IndexError would be raised.
        :return:the nucleotide in specifies place of the dna sequence.
        """
        if index >= self.__len__():
            raise IndexError
        return self.get_dna_sequence()[index]

    def __setitem__(self, index, value):
        """
        :param index:an index if not exist IndexError would be raised.
        :return:the nucleotide in specifies place of the dna sequence.
        """
        if index >= self.__len__():
            raise IndexError
        new_seq = self.get_dna_sequence()
        new_seq[index] = value
        self.set_dna_sequence(new_seq)

    def __len__(self):
        """
        :return: the length of the dna sequence.
        """
        return len(self.__dna_sequence)

    def assighment(self, dna_sequence):
        if hasattr(dna_sequence, 'get_dna_sequence'):
            return self.__dna_sequence == dna_sequence.get_dna_sequence()
        elif isinstance(dna_sequence, str):
            return self.get_dna_sequence() == dna_sequence
