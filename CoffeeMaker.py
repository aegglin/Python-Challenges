"""
Abstraction of a Coffee Maker. Prompts user
for what they want, reports remaining resources,
checks if resources are sufficient, processes coins, and
checks if transactions are successful. There are 3 options
to order -- espresso, latte, cappuccino, each with their own
cost, milk, coffee, and water amounts that are necessary.  
"""


class CoffeeMaker:
    def __init__(self):
        """Creates a CoffeeMaker object."""
        self.money = 0
        self.coffee_prices = {'espresso': 1.50, 'latte': 2.50, 'cappuccino': 3.00}
        self.curr_ingredients = {'water': 300, 'milk': 200, 'coffee': 100}
        self.ingredient_requirements = {'espresso': {'water': 50, 'milk': 0, 'coffee': 18},
                                        'latte': {'water': 200, 'milk': 150, 'coffee': 24},
                                        'cappuccino': {'water': 250, 'milk': 100, 'coffee': 24}}

    def report(self):
        """Displays the amount left of each ingredient."""
        for ingredient, curr_amt in self.curr_ingredients.items():
            unit = 'g' if ingredient == 'coffee' else 'ml'
            print(f'{ingredient.title()}: {curr_amt}{unit}')
        print('Money: ${:.2f}'.format(self.money))

    def check_resources(self, coffee_name):
        """Returns True if there is sufficient amount of each resource."""
        for ingredient, req in self.ingredient_requirements[coffee_name].items():
            if req > self.curr_ingredients[ingredient]:
                print(f'Sorry, there is not enough {ingredient}.')
                return False
        if coffee_name in self.coffee_prices:
            return True

        return False

    def get_coin_total(self, coin_name):
        """Returns the amount of change inputted for one coin."""
        while True:
            num = input(f"How many {coin_name}? ")
            try:
                num = int(num)
            except ValueError as e:
                print("Invalid input. Try again.")
            else:
                break
        if coin_name == 'quarters':
            num *= .25
        elif coin_name == 'dimes':
            num *= .1
        elif coin_name == 'nickels':
            num *= .05
        elif coin_name == 'pennies':
            num *= .01
        return num

    def process_coins(self):
        """Return the total amount of change inputted."""
        print("Please insert coins.")
        total_given = 0
        for coin in ['quarters', 'dimes', 'nickels', 'pennies']:
            total_given += self.get_coin_total(coin)
        print("Total amount given is: ${:.2f}".format(total_given))
        return total_given

    def check_transaction(self, total_given, coffee_name):
        """Return True if the proper amount of change for the given drink was inputted."""
        price = self.coffee_prices[coffee_name]
        if total_given < price:
            print('Sorry, that\'s not enough money. Money refunded.')
            return False
        else:
            if total_given > price:
                print("Here is ${:.2f} in change.".format(total_given-price))
            return True

    def make_coffee(self, coffee_name):
        """Subtracts relevant ingredient amounts from each ingredient category."""
        # Espresso -- 250ml water, 18g coffee. $1.50
        # Latte -- 200ml water, 24g coffee, 150ml milk. $2.50
        # Cappuccino -- 250ml water, 24g coffee, 100ml milk. $3.00
        for ingredient in self.curr_ingredients.keys():
            self.curr_ingredients[ingredient] -= self.ingredient_requirements[coffee_name][ingredient]

        self.money += self.coffee_prices[coffee_name]
        print("Here is your latte. Enjoy!")
