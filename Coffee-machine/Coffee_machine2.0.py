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
user_change = 0
resources = {
    "water": 500,
    "milk": 300,
    "coffee": 200,
}


def resources_sufficient(products):
    for item in products:
        if products[item] > resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True


def coins_inserted():
    total = int(input("Insert quarters: ")) * 0.25
    total += int(input("Insert $1 bills: ")) * 1.00
    return total


def transaction(money, selected_drink):
    if money >= selected_drink:
        change = round(money - selected_drink, 2)
        # print(f"Here is a ${change} in change")
        global profit
        profit += selected_drink
        global user_change
        user_change += change
        return True
    elif money < selected_drink:
        if user_change > selected_drink:
            user_change -= selected_drink
            return True
        else:
            print("Not enough money...")
            return False


def make_coffee(selected_coffee, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Take your {selected_coffee}. Enjoy!")


def take_change():
    global user_change
    user_change -= user_change
    print(f"Withdrew money. You have ${user_change} change")


working = True
while working:
    print(f"You have: ${user_change} change")
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        take_change()
        working = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Profit: ${profit}\n")
    else:
        order = MENU[choice]
        if resources_sufficient(order["ingredients"]):
            payment = coins_inserted()
            if transaction(payment, order["cost"]):
                make_coffee(choice, order["ingredients"])
