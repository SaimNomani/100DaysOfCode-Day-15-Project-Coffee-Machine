MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "water": 1000,
    "milk": 500,
    "coffee": 100,
}


def get_report():
    for resource in resources:
        print(f'{resource}: {resources[resource]}')
    print(f'money: {money}')


def is_sufficient(coffee_type):
    if coffee_type == 'espresso':
        if resources['water'] < (MENU[coffee_type]["ingredients"]["water"]) or resources['coffee'] < MENU[coffee_type]["ingredients"]["coffee"]:
            return False
        else:
            return True
    elif coffee_type == 'latte':
        if resources['water'] < (MENU[coffee_type]["ingredients"]["water"]) or resources['coffee'] < MENU[coffee_type]["ingredients"]["coffee"] or resources['milk'] < MENU[coffee_type]["ingredients"]["milk"]:
            return False
        else:
            return True
    elif coffee_type == 'cappuccino':
        if resources['water'] < (MENU[coffee_type]["ingredients"]["water"]) or resources['coffee'] < MENU[coffee_type]["ingredients"]["coffee"] or resources['milk'] < MENU[coffee_type]["ingredients"]["milk"]:
            return False
        else:
            return True


def is_transaction_successful(coffee_type):
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25
    print("Please insert coins: \n")
    no_of_quarters = (float(input("How many quarters: "))) * quarter
    no_of_dimes = (float(input("How many dimes: "))) * dime
    no_of_nickles = (float(input("How many nickles: "))) * nickel
    no_of_pennies = (float(input("How many pennies: "))) * penny
    total_in_dollars = no_of_quarters + no_of_dimes + no_of_nickles + no_of_pennies
    change = total_in_dollars - MENU[coffee_type]['cost']
    if total_in_dollars >= MENU[coffee_type]['cost']:
        print(f"here is your ${round(change, 2)} change")
        updated_money = update_resources(coffee_type)
        return updated_money
    else:
        return -1


def update_resources(coffe_type):
    resources['water'] -= MENU[coffe_type]['ingredients']['water']
    resources['coffee'] -= MENU[coffe_type]['ingredients']['coffee']
    resources['milk'] -= MENU[coffe_type]['ingredients']['milk']
    return MENU[coffe_type]['cost']


def generate_menu():
    return input('''\nType "1" to order your coffee\nType "2" to generate report\nType "3" to turn off the machine\n''')


money = 0
should_order = True
password = 1234
while True:
    main_menu = generate_menu()
    if main_menu == '1':
        while should_order:
            order = (input("What would you like? (espresso, latte, cappuccino): ")).lower()
            if is_sufficient(order):
                money_earned = is_transaction_successful(order)
                if money_earned != -1:
                    print(f"Here is your {order}, enjoy")
                    money += money_earned
                else:
                    print("Sorry, that's not enough money. Money refunded")
            else:
                print(f"Sorry, resources are not sufficient to prepare {order}")
            another_coffee = input("Type '1' to order another coffee\nType '2' to go back\n")
            if another_coffee == '2':
                should_order = False
    elif main_menu == '2':
        if int(input("Enter password: ")) == 1234:
            get_report()
        else:
            print("Wrong password")
    elif main_menu == '3':
        if int(input("Enter password: ")) == 1234:
            break
        else:
            print("Wrong password")
