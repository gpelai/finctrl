class Menu:
    def __init__(self):
        pass

    def menu_msg(self, menu_title):
        crud_msg = """##### CRUD MENU #####
    1. Create
    2. Read
    3. Update
    4. Delete"""

        financial_msg = """##### FINANCIAL MENU #####
    1. Income
    2. Outcome"""
        
        match menu_title:
            case "crud":
                print(crud_msg)
            case "financial":
                print(financial_msg)
    
    def input_collect(self):
        opt = input("\nChoose an option above: ")
        return opt


    def input_check(self, menu_title:str, option:int):
        crud_options = [1,2,3,4]
        financial_options = [1,2]
        match menu_title:
            case "menu_crud":
                if option in crud_options:
                    return True
                else:
                    print("Wrong option, please try again!\n")
                    return False
                
            case "menu_financial":
                if option in financial_options:
                    return True
                else:
                    print("Wrong option, please try again!\n")
                    return False