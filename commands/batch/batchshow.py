from data_base.db_batch import DB_batches


class Batchshow:
    def __init__(self, name, none="None"):
        if name == "None" or none != "None":
            raise ValueError("not enough arguments.")
        if not name.startswith("@"):
            raise ValueError("name has to start with @.")
        self.name = name[1:]
    def execute(self):
        try:
            return DB_batches.get_batch(self.name)
        except Exception as err:
            return err
