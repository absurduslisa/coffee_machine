MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

should_work = True


def check_resources(ingredients, price, order):
    for key in ingredients:
        if resources[key] < ingredients[key]:
            return f'Sorry there is not enough {key}'
        else:
            count_money(price, ingredients, order)


def count_money(price, ingredients, order):
    """Counts how much money user inserted, gives change or returns if not enough"""

    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))

    users_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    difference = round((price - users_money), 2)
    if difference > 0:
        return "Sorry that's not enough money. Money refunded."
    else:
        resources['money'] += price
        for key in ingredients:
            resources[key] -= ingredients[key]
        return f"Here is ${difference * -1} in change. \nHere is your {order}. Enjoy!"


def make_an_order():
    """Asks user what he wants, creates an order"""
    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order == 'report':
        for key in resources:
            print(f'{key}: {resources[key]}')
        return

    ingredients = MENU[order]['ingredients']
    price = MENU[order]['cost']
    checked_resources = check_resources(ingredients, price, order)
    print(checked_resources)


while should_work:
    make_an_order()

# TODO: Turn off the Coffee Machine by entering “off” to the prompt
should_work = False

