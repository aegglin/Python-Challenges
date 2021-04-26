import CoffeeMaker


def get_user_input():
    """Gets the user input for a CoffeeMaker"""
    # Use a breakpoint in the code line below to debug your script.
    user_input = ""
    cm = CoffeeMaker.CoffeeMaker()

    while user_input != "stop":
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == "report":
            cm.report()
        elif user_input in ["espresso", "latte", "cappuccino"]:
            resource_check = cm.check_resources(user_input)
            if not resource_check:
                continue;
            else:
                amt_given = cm.process_coins()
                transac_result = cm.check_transaction(amt_given, user_input)
                if transac_result:
                    cm.make_coffee(user_input)
        elif user_input != 'stop':
            print('Sorry, unrecognized coffee specified.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_user_input()
