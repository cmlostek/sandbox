# creating an inventory list

inventory = []
inventory_items = {}


def start_inventory():
    print("This will start a new inventory list. \n")
    while True:
        item = input("Please input an item. \n")
        amount = input("Please input the amount of this item. \n")
        inventory_items[item] = amount
        if item == "":
            break
    print(inventory_items)


start_inventory()
