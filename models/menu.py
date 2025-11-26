import sys

class Menu:
    def __init__(self, title):
        self.title = title

        self.messages = {
            "crud":"\n##### CRUD MENU #####\n1. Create\n2. Read\n3. Update\n4. Delete\n0. Exit",
            "financial":"\n##### FINANCIAL MENU #####\n1. Income\n2. Outcome\n0. Exit"
        }

        self.options = {
            "crud":["1","2","3","4"],
            "financial":["1","2"]
        }

    def msg(self):
        print(self.messages[self.title])
    
    def collect(self):
        opt = input("\nChoose an option above: ")
        return opt

    def check_option(self, option:int):

        allowed_options = self.options[self.title]

        if option in allowed_options:
            return True
        elif option == "0":
            print("Exiting progam! Bye! :)")
            sys.exit()
        else:
            print("Wrong option, please try again!")
            return False
