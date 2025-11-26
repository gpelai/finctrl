from .system import System
sys = System()

class Menu:
    def __init__(self):
        self.message = ""
        self.error = ""
        self.options = []

    def msg(self):
        sys.clear()
        print("=========== FINCTRL ===========")
        print("        PRESS 0 TO EXIT        \n")
        print(self.message)

        if self.error:
            print(f"\n{self.error}")
    
    def collect(self):
        opt = input("\nChoose an option above: ")
        return opt

    def check_option(self, option):

        try:
            option = int(option)
        except ValueError:
            self.error = "[WARNING] Option need to be numerical."
            return False

        if option in self.options:
            return True
        elif option == 0:
            sys.exit()
        else:
            self.error = "[WARNING] Option need to be in the menu."
            return False

class MenuCrud(Menu):
    def __init__(self):
        super().__init__()
        self.message = "##### CRUD MENU #####\n1. Create\n2. Read\n3. Update\n4. Delete"
        self.options = [1,2,3,4]

class MenuFinancial(Menu):
    def __init__(self):
        super().__init__()
        self.message = "##### FINANCIAL MENU #####\n1. Income\n2. Outcome"
        self.options = [1,2]
