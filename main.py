from models.menu import MenuCrud, MenuFinancial

# MODELS
menu_crud = MenuCrud()
menu_financial = MenuFinancial()

# MAIN
if __name__=="__main__":

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
    
    options_chosen = {
        "crud": option_crud,
        "financial": option_financial
    }
