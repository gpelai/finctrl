import os
from models.menu import Menu

menu_crud = Menu("crud")
menu_financial = Menu("financial")

menu_workflow = ["crud", "financial"]

if __name__=="__main__":
    print("=========== FINCTRL ===========")
    print("      press ctrl+c to exit     ")

    while True:
        menu_crud.msg()
        option_crud = menu_crud.collect()

        if menu_crud.check_option(option_crud):
            break

    while True:
        menu_financial.msg()
        option_financial = menu_financial.collect()

        if menu_financial.check_option(option_financial):
            break

    print("============= END =============")