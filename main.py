menu_crud = """--- CRUD OPTION ---
    1. Create
    2. Read
    3. Update
    4. Delete

Choose an crud option: """

menu_financial = """--- FINANCIAL OPTION ---
    1. Income
    2. Outcome

Choose a financial option: """

if __name__=="__main__":
    print("=========== FINCTRL ===========")
    print("      press ctrl+c to exit     \n")

    opt_crud = input(menu_crud)
    print("\n-------------------------------\n")
    opt_financial = input(menu_financial)

    print("============= END =============")