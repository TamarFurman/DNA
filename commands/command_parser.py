def parser_creation(command):
    if not isinstance(command, str):
        raise ValueError("accepted string only")
    if len(command.split()) < 2:
        raise ValueError("not enough arguments.")
    split_c = command.split()
    if len(split_c) == 2:
        split_c.append("None")
    return split_c


def parser_manipulation(command):
    if not isinstance(command, str):
        raise ValueError("accepted string only.")
    elif len(command.split()) < 2:
        raise ValueError("not enough arguments.")
    split_seq = command.split(":") if len(command.split(":")) > 1 else [command, "None"]
    splitted = split_seq[0].split(" ", 1)
    return splitted + [split_seq[-1]]


def parser_management(command):
    if not isinstance(command, str):
        raise ValueError("accepted string only")
    elif len(command.split()) < 2:
        raise ValueError("not enough arguments.")
    split_name = command.split()
    return split_name if len(split_name) == 3 else split_name + ["None"]


def parser_batch(command, save=None):
    if not isinstance(command, str):
        raise ValueError("accept string only.")
    elif len(command.split()) > 2 and save is None:
        raise ValueError("too match arguments.")
    elif len(command.split()) < 1:
        raise ValueError("not enough arguments.")
    split_name = " ".join(command.split(":"))
    split_name = split_name.split()
    if save == "save":
        return split_name if len(split_name) == 3 else split_name + ["None"]
    return split_name if len(split_name) == 2 else split_name + ["None"]
