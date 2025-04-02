from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

allowed_options = (menu.get_items() + "off/report").split('/')

while True:
    try:
        option = input(f"What would you like? ({menu.get_items()}): ").lower()
        if option in allowed_options:
            if option=="off":
                break
            elif option=="report":
                print(coffee_maker.report())
                print(money_machine.report())
            else:
                drink = menu.find_drink(option)
                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else: raise Exception
    except:
        print("Option not allowed, please try again...")
print("Ending Machine...")