from List_Tracker import menu as m
print("-------------")

# Asks the user for the choice from the menu and then runs that choice using the case match
m.menu()
choice = input("Please input your choice. \n")
match choice:
    case "1":
        from functions import start_list
        start_list()
    case "2":
        from functions import update_list
        update_list()
    case "3":
        from functions import start_list
        start_list()
    case "4":
        from functions import save_list
        save_list()
    case "5":
        from functions import get_list
        get_list()
    case "6":
        from functions import load_list
        load_list()
    case "7":
        print("Thank you for using this program. Goodbye.")
    case _:
        print("This is not a valid response. Please input a number from 1 to 7. \n")
