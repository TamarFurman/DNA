from data_base.db_batch import DB_batches


class Batchsave:
    def __init__(self, name, file_name):
        if name == "None":
            raise ValueError("not enough arguments.")
        else:
            if not name.startswith("@"):
                raise ValueError("name has to start with @.")
            self.name = name[1:]
        self.file_name = file_name

    def execute(self):
        try:
            if self.file_name == "None":
                self.file_name = f"{self.name}.dnabatch"
            commands = DB_batches.get_batch(self.name)
            print(commands)
            with open(self.file_name, "w+") as file:
                file.write('\n'.join(commands) + '\n')
        except Exception as err:
            print(err)
