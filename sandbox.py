items = []
print("-------------")
print("You will add items to the list, this will be followed by a prompt to update the item.")
while True:
    x = input("Please add an item to the list. Input a blank enter to stop.")
    if x == "":
        break
    else:
        items.append(x)
print(items)
print("-------------")
update = input("If this list is correct press enter, otherwise enter yes to edit the list.")

if update == "Y" or update == "y" or update == "yes" or update == "Yes" or update == "YES":
    print("You will now update the list.")
    for i in range(len(items)):
        print(i, items[i])
        x = input("Would you like to update this item?")
        if x == 'yes' or x == 'Yes':
            items[i] = input("What would you like to update it to? Input a new string or use a blank enter to delete "
                             "the item.")
            print(items)
        elif x == 'no' or x == 'No':
            print("-------------")
    print(items)
else:
    print(items)
    print("-------------")
