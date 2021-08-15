from data_base.db_batch import DB_batches


class Batch_Creation:
    def __init__(self, name, none="None"):
        if name == "None" or none != "None":
            raise ValueError("not enough arguments")
        self.name = name

    def execute(self):
        try:
            DB_batches.add_batch(self.name)
        except Exception as err:
            return err
        user_input = ''
        while user_input != "end":
            user_input = input("> batch >>> ")
            if user_input != "end":
                try:
                    DB_batches.add_to_batch(self.name, user_input)
                except Exception as err:
                    print(err)
        return
