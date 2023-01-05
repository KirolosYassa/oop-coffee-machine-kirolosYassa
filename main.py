from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drinks = [MenuItem("espresso", 100, 50, 25, 2.5),
          MenuItem("latte", 75, 150, 18, 2.5),
          MenuItem("cappuccino", 120, 100, 15, 2.5)]

me = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()


def report():
    return Menu.get_items(self=me)


def process_order(cup):
    if coffee_maker_obj.is_resource_sufficient(cup):
        if money_machine_obj.make_payment(cup.cost):
            coffee_maker_obj.make_coffee(cup)


again = True
while again:

    choice = input(f"Drink?\n{report()}?:    ")
    if choice == "report":
        print(coffee_maker_obj.report())
        continue
    try:
        cup = me.find_drink(choice)
        process_order(cup)
    except:
        print("Incorrect input!...\nPlease try again...")
        continue

    again = input("Want another drink? Type 'y' for YES/ 'n' for NO?:    ")
    if again.lower() != "y":
        again = False


print(coffee_maker_obj.report())
