menu = ("Please select an option from the menu below: \n"
        "1: Start a list. \n"
        "2: Update a list. \n"
        "3: Add more items to the list. \n"
        "4: Save the list to a text file. \n"
        "5: Get the list \n"
        "6: Load the list from a file \n"
        "7: Exit the program \n")

items = []
print("-------------")

# Function to start a list


def start_list():
    print("You will add items to the list, this will be followed by a prompt to update the item.")
    while True:
        x = input("Please add an item to the list. Input a blank enter to stop. \n")
        if x == "":
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


# Asks the user for the choice from the menu
while True:
    print(menu)
    menu_choices = [1, 2, 3, 4, 5, 6, 7]
    menu_choices_str = [str(i) for i in menu_choices]
    try:
        choice = int(input("Which item from the list would you like to do? \n"))
        i = choice
        if i in menu_choices:
            if i == 1:  # start list
                start_list()
            elif i == 2:  # update list
                update_list()
            elif i == 3:  # add more items to list
                start_list()
            elif i == 4:  # save list to text file
                save_list()
            elif i == 5:  # Get the list
                get_list()
            elif i == 6:  # Load list from file
                load_list()
            elif i == 7:  # exit the program
                print("You have exited the list editor.")
                break
            else:
                continue
    except ValueError:
        print("This is not a valid response. Please input a number from the menu options:", ", ".join(menu_choices_str))
        continue
