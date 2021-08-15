from data_base.db_batch import DB_batches


class Batchlist:
    def __init__(self, name, none="None"):
        if name != "None" or none != "None":
            raise ValueError("too match arguments.")

    def execute(self):
        try:
            return list(DB_batches.get_keys())
        except Exception as err:
            return err
