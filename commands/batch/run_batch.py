from data_base.db_batch import DB_batches
from invoker import Invoker


class Run_Batch:
    def __init__(self, name, none="None"):
        if name == "None" or none != "None":
            raise ValueError("not enough arguments.")
        if not name.startswith("@"):
            raise ValueError("name has to start with @.")
        self.name = name[1:]
        self.invoker = Invoker()

    def execute(self):
        batch_commands = DB_batches.get_commands_of_batch(self.name)
        for command in batch_commands:
            self.invoker.run(command)
        try:
            return DB_batches.get_batch(self.name)
        except Exception as err:
            return err
