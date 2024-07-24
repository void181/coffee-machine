MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 200,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_cash():
    """Returns the total calculated from coins inserted."""
    print("Please insert cash.")
    total = int(input("how many cash*100?: ")) * 100 # 1*100=100

    return total


def is_transaction_successful(total, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if total >= drink_cost:
        change = round(total - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_cash()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("invalid choices ")







