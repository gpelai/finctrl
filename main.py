from models import Menu

menu = Menu()
opt_crud_status = False
opt_financial_status = False

menu_workflow = ["crud", "financial"]

if __name__=="__main__":
    print("=========== FINCTRL ===========")
    print("      press ctrl+c to exit     \n")

    opt_list = []

    for m in menu_workflow:
        menu.menu_msg(m)
        opt = menu.input_collect()
        opt_tuple = (m, opt)
        opt_list.append(opt_tuple)
        print("\n-------------------------------\n")

    print(opt_list)


    print("============= END =============")