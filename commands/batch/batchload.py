from data_base.db_batch import DB_batches


class Batchload:
    def __init__(self,file_name, name):
        if name != "None":
            if not name.startswith("@"):
                raise ValueError("name has to start with @.")
            self.name = name[1:]
        else:
            self.name = name
        if file_name == "None":
            raise ValueError("not enough arguments.")
        self.file_name = file_name

    def execute(self):
        if ".dnabatch" not in self.file_name:
            self.file_name += ".dnabatch"
        if self.name == "None":
            self.name = self.file_name.rpartition(".")[0]
        with open(self.file_name,"r") as file:
            batch = "".join(file.readlines())
            batch = batch.split("\n")[:-1]
        try:
            DB_batches.add_batch(self.name)
            DB_batches.add_batch_list(self.name,batch)
        except Exception as err:
            print(err)
