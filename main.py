from models import Menu

menu = Menu()
menu_workflow = ["crud", "financial"]

if __name__=="__main__":
    print("=========== FINCTRL ===========")
    print("      press ctrl+c to exit     ")

    option_list = []
    option_check = False

    for m in menu_workflow:
        
        while option_check == False:
            menu.menu_msg(m)
            option = menu.collect()
            option_check = menu.check_option(m, option)

        option_tuple = (m, option)
        option_list.append(option_tuple)
        print("-------------------------------")

    print(option_list)


    print("============= END =============")