import os

class System:
    def __init__(self):
        pass

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")