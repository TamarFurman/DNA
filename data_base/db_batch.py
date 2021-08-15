class DB_batches:
    batches = dict()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not DB_batches.__instance:
            DB_batches.__instance = object.__new__(cls)
        return DB_batches.__instance

    @staticmethod
    def add_batch(batch_name):
        if not isinstance(batch_name, str):
            raise ValueError("excepted batch name as string.")
        if batch_name in DB_batches.batches:
            raise KeyError("batch already exist.")
        DB_batches.batches[batch_name] = []

    @staticmethod
    def add_to_batch(batch_name,command):
        if not isinstance(batch_name, str):
            raise ValueError("excepted batch name as string.")
        if batch_name not in DB_batches.batches:
            raise KeyError("batch doesn't exist.")
        DB_batches.batches[batch_name].append(command)

    @staticmethod
    def add_batch_list(batch_name, commands):
        if not isinstance(commands, list):
            raise ValueError("excepted batch commands as list.")
        if batch_name not in DB_batches.batches:
            raise KeyError("batch doesn't exist.")
        DB_batches.batches[batch_name] = commands
    @staticmethod
    def get_commands_of_batch(batch_name):
        if not isinstance(batch_name, str):
            raise ValueError("excepted batch name as string.")
        if batch_name not in DB_batches.batches:
            raise KeyError("batch doesn't exist.")
        return DB_batches.batches[batch_name]

    @staticmethod
    def get_command_of_batch(batch_name):
        if not isinstance(batch_name, str):
            raise ValueError("excepted batch name as string.")
        if batch_name not in DB_batches.batches:
            raise KeyError("batch doesn't exist.")
        return DB_batches.batches[batch_name].pop()

    @staticmethod
    def get_keys():
        return DB_batches.batches.keys()

    @staticmethod
    def get_values():
        return DB_batches.batches.values()

    @staticmethod
    def get_batch(name):
        if name not in DB_batches.batches:
            raise KeyError("batch not exist.")
        return DB_batches.batches[name]