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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def is_enough_resources(type_coffee):
    ingredients = MENU[type_coffee]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_payment(cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))


    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif total > cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")

    return True


def make_coffee(type_coffee):
    ingredients = MENU[type_coffee]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {type_coffee}. Enjoy!")


def report():
    print("\nCurrent resource levels:")
    unit =""
    for key, value in resources.items():
        if key in ["water", "milk"]:
            unit = "ml"
        elif key == "coffee":
            unit = "g"
        else:
            unit = "$"
        print(f"{key.capitalize()}: {value}{unit}")


def coffee_machine():

    while True:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino/report/off): ").lower()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break

        elif choice == "report":
            report()

        elif choice in MENU:
            if is_enough_resources(choice):
                cost = MENU[choice]["cost"]
                if process_payment(cost):
                    make_coffee(choice)
        else:
            print("Invalid input. Please try again.")


coffee_machine()
