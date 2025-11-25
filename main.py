from models.menu import Menu
from models.system import System

# MODELS
sys = System()
menu_crud = Menu("crud")
menu_financial = Menu("financial")

# VARS
menu_workflow = ["crud", "financial"]

# MAIN
if __name__=="__main__":

    while True:
        sys.clear()
        print("=========== FINCTRL ===========")
        print("      press ctrl+c to exit     ")
        menu_crud.msg()
        option_crud = menu_crud.collect()

        if menu_crud.check_option(option_crud):
            break

    while True:
        sys.clear()
        print("=========== FINCTRL ===========")
        print("      press ctrl+c to exit     ")
        menu_financial.msg()
        option_financial = menu_financial.collect()

        if menu_financial.check_option(option_financial):
            break
    
    options_chosen = {
        "crud": option_crud,
        "financial": option_financial
    }

    sys.clear()
    print(options_chosen)