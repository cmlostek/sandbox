items = []


def start_list():
    print("You will add items to the list, this will be followed by a prompt to update the item.")
    while True:
        x = input("Please add an item to the list. Input a blank enter to stop. \n")
        if x == "":
            y = input("Would you like to save this list? \n")
            match y.lower():
                case "yes":
                    save_list()
                    break
                case "no":
                    break
                case _:
                    print("This is not a valid response. Please input yes or no")
            break
        else:
            items.append(x)
            continue
    print(items)
    print("-------------")


def update_list():
    print(items)
    update = input("If this list is correct press enter, otherwise enter yes to edit the list. \n")
    update_lower = update.lower()
    if update_lower == "yes":
        print("You will now update the list.")

        # For loop to go through every item in list
        for n in range(len(items)):
            print(n, items[n])
            x = input("Would you like to update this item? \n")
            x_lower = x.lower()
            if x_lower == 'yes':
                items[n] = input(
                    "What would you like to update it to? Input a new string or use a blank enter to delete "
                    "the item. \n")
                print(items)
            elif x_lower == 'no':
                continue
            else:
                print("This is not a valid response. Please input yes or no")
        print(items)
        print("-------------")
    else:
        print(items)
        print("-------------")


def get_list():
    print("This is your list: ", items)


def save_list():
    with open("list.txt", "w") as file_:
        for item in items:
            file_.write(item + "\n")
        print("Your list has been saved to the file 'list.txt' ")
        print("-------------")


def load_list():
    with open("list.txt", "r") as file_:
        for item in file_.readlines():
            items.append(item.strip())
        print("Your list has been loaded from the file 'list.txt' ")
        print("-------------")
