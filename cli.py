from invoker import Invoker


class CLI:
    """
    The command line interface allows interaction with the user. Throughout that
    interface, the user can enter their input and see the application's outputThe
    command line interface allows interaction with the user. Throughout that
    interface, the user can enter their input and see the application's output
    """
    def __init__(self):
        self.command = ""
        self.invoker = Invoker()

    def run(self):
        """
        This run function get command from the user and call to invoker run that will perform it,according to it's type.
        """
        while True:
            self.command = input("> cmd >>> ")
            self.invoker.run(self.command)


if __name__ == '__main__':
    CLI().run()
