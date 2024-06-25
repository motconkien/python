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
    "milk" : 200,
    "coffee": 100
}

def is_resource_sufficient(ingredients):
    """Check the ingredients dictionary of each drink"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print("sorry there is not enough {item]")
            return False
    return True

def process_coin():
    """Return total calculated from coins"""
    print("Please insert coins")
    quarters = int(input("How many quarters? "))*0.25
    dimes = int(input("How many dimes? "))*0.10
    nickles = int(input("How many nickles? "))*0.05
    pennies = int(input("How many pennies? "))*0.01

    total = quarters + dimes + nickles + pennies
    return round(total,2)

def is_transaction_successful(money, cost):
    """Return true when payment is accepted"""
    if money > cost:
        change = round(money - cost,2)
        global profit
        profit += money
        print(f"Here is {change} dollars in change")
        return True
    else:
        print( "That is not enough to place orders. Money refunded")
        return False

def make_coffee(coffee, ingredients):
    """Deduct the required ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee}")

is_on = True
while is_on:
    promte = input("What would you like? (espresso/latte/cappuccino)\n")
    
    if promte == "off":
        is_on = False
    elif promte == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Profit: {profit}")
    else:
        drink = MENU[promte]
        if is_resource_sufficient(drink["ingredients"]):
            total = process_coin()
            if is_transaction_successful(total, drink["cost"]):
                make_coffee(promte, drink["ingredients"])