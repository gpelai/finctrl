class Menu:
    def __init__(self):
        pass

    def menu_msg(self, menu_title):
        crud_msg = """\n##### CRUD MENU #####
    1. Create
    2. Read
    3. Update
    4. Delete"""

        financial_msg = """\n##### FINANCIAL MENU #####
    1. Income
    2. Outcome"""
        
        match menu_title:
            case "crud":
                print(crud_msg)
            case "financial":
                print(financial_msg)
    
    def collect(self):
        opt = input("\nChoose an option above: ")
        return opt


    def check_option(self, menu_title:str, option:int):

        crud_options = [1,2,3,4]
        financial_options = [1,2]

        match menu_title:
            case "crud":
                if option in crud_options:
                    print("Right option!")
                    return True
                else:
                    print("Wrong option, please try again!")
                    return False
                
            case "financial":
                if option in financial_options:
                    print("Right option!", option)
                    return True
                else:
                    print("Wrong option, please try again!")
                    return False

