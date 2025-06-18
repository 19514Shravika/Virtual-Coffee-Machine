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
            "coffee": 24,                                    #function-1 (check for resources)
        },                                                   #function-2 (check with the payment, if successful)
        "cost": 2.5,                                         #function-3 (make coffee- because payment is made)
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
}
def check_resources(order):
    for item in MENU[order]["ingredients"]:
        if resources[item]<MENU[order]["ingredients"][item]:
            print("Sorry, there are no sufficient resources 😨")
            return False
    return True

def payment_process(cost):
    print("Insert coins 🪙")
    quarters_coins=int(input("How many quarters u are inserting"))
    dimes_coins=int(input("How many dimes u are inserting"))
    nickels_coins=int(input("How many nickels u are inserting"))
    pennies_coins=int(input("How many pennies u are inserting"))
    dollar_value=(quarters_coins*0.25)+(dimes_coins*0.10)+(nickels_coins*0.05)+(pennies_coins*0.01)
    if dollar_value<cost:
        print("You paid less than drink cost 😔, money will be refunded")
        return None
    else:
        change=round(dollar_value-cost,2)
        if change>0:
            print(f"Here is your change: ${change} 💸")
        return cost

def make_coffee(order):
    for item in MENU[order]["ingredients"]:
        resources[item]-=MENU[order]["ingredients"][item]
    print("Here is your drink ☕")

money=0
machine_running=True
while machine_running:
    drink=input("What would you like? (espresso/latte/cappuccino)🥫")
    enough_resource = True
    if drink=="off":
        print("**TIME UP** 🆙")
        machine_running=False
    elif drink=="report":
        print("Here is the available report 🗎")
        print(f"water: {resources['water']}ml, milk: {resources['milk']}ml, coffee: {resources['coffee']}ml, money: ${money}")
    elif drink in MENU:
        if check_resources(drink):
            payment=payment_process(MENU[drink]["cost"])
            if payment is not None:
                money+=payment
                make_coffee(drink)
    else:
        print("Invalid selection..😕")
