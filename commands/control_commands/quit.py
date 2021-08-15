from data_base.db import DB_sequences
from data_base.dna_status import DB_status


class Quit:
    def __init__(self):
        self.user_input = ""

    def execute(self,com):
        news = DB_status.get_new_status()
        modified = DB_status.get_modified_status()
        print(self.msg(modified,news))
        while self.user_input.upper() not in ['Y', 'N']:
            self.user_input = input("> confirm >>>")
            if self.user_input.upper() not in ['Y', 'N']:
                print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
        if self.user_input.upper() == 'Y':
            print("Thank you for using Dnalanyzer.\nGoodbye!")
            exit(0)
        return

    def msg(self,n1,n2):
        return f"There are {n1} modified and {n2} new sequences. Are you sure you want to quit?\n" \
                   "Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'."

