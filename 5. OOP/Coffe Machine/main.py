from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
Is_On = True
while Is_On:
    user_input = input("What would you like? (espresso/ latte/ cappuccino)")
    if user_input == "off":
        Is_On = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        check_drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(check_drink) and money_machine.make_payment(check_drink.cost):
            coffee_maker.make_coffee(check_drink)