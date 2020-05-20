import calculation

def help():
    """
    Outputing s help description on the screen
    :return:
    """
    print(
        """\n****************************************\nFormat for adding items: 'a,Item Name, Item Number, Item price'\n****************************************
           \n****************************************\nFormat for seling items: 's,Item Name, Item Number'\n****************************************\n""")

#Display total number and total value of inventory
def current_stock(inventory):
    if inventory:
        for oneDict in inventory:
            for k, v in oneDict.items():
                print("{} : {}" .format(k, v))
            print("*" * 10)
            sumOfStock, sumOfValue = calculation.get_current_stock(inventory)

        print("*** Total stock is: {}. ***" .format(sumOfStock))
        print("*** Total stock value: {}$. ***".format(sumOfValue))

    else:
        print("Inventory is empty!")

def try_again():
    print("Please try again. I don't understand.")

def main():
    inventory = calculation.load_from_file()

    while True:
        user_input = input("Choices:\n[H] for [H]elp on information how to Add or Sell items.\n[A] and amount to [A]dd.\n[S] and amount to [S]ell\n[L] to [L]ist current stock\n[x] for E[x]it.\nEnter command: ")
        user_input = user_input.upper()

        #On exit show current stock and break
        if user_input[0] == "X":
            print("Good bye !")
            break

        elif user_input[0] == "H":
            help()

        #Show current stock
        elif user_input[0] == "L":
            current_stock(inventory)

        #On Add stock call add function from calculation module
        elif user_input[0] == "A":
            inventory = calculation.add(user_input, inventory)

        # On Sell stock call sell function from calculation module
        elif user_input[0] == "S":
            inventory = calculation.sell(user_input, inventory)
        else:
            try_again()

    #Save current inventory situation for later use
    calculation.save_to_file(inventory)

if __name__=="__main__":
    main()