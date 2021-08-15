class DB_status:
    dna = dict()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not DB_status.__instance:
            DB_status.__instance = object.__new__(cls)
        return DB_status.__instance

    @staticmethod
    def add_dna(dna_id, status="new"):
        if not isinstance(dna_id, int):
            raise ValueError("excepted id of dna as int.")
        if dna_id in DB_status.dna:
            raise KeyError("dns already exist.")
        DB_status.dna[dna_id] = status

    @staticmethod
    def update_status(dna_id, status=None):
        if not isinstance(dna_id, int):
            raise ValueError("excepted id of dna as int.")
        if not status in ["up to date", "modified", "new",None]:
            raise ValueError("Invalid status.")
        if dna_id not in DB_status.dna:
            raise KeyError("dna doesn't exist.")
        if status is None:
            if DB_status.dna[dna_id] == "up to date":
                DB_status.dna[dna_id] = "modified"
                return
        else:
            DB_status.dna[dna_id] = status

    @staticmethod
    def get_status(dna_id):
        if not isinstance(dna_id, int):
            raise ValueError("excepted id of dna as int.")
        if dna_id not in DB_status.dna:
            raise KeyError("dna doesn't exist.")
        return DB_status.dna[dna_id]

    @staticmethod
    def get_all_status():
        return DB_status.dna.values()

    @staticmethod
    def get_new_status():
        all_status = DB_status.get_all_status()
        return sum(status == "new" for status in all_status)

    @staticmethod
    def get_modified_status():
        all_status = DB_status.get_all_status()
        return sum(status == "modified" for status in all_status)