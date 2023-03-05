import easygui
button = ""


#MAIN DICTIONARY CONTAINING THE MENU
menu={
    "super":{
        "Cheeseburger":6.69,
        "Large Fries": 2,
        "Smoothie": 2},

    "cheezy": {
        "Cheeseburger":6.69,
        "Fries": 1,
        "Fizzy Drink": 1 },

    "value": {
        "Beef Burger": 5.69,
        "Fries": 1,
        "Fizzy Drink": 1}
}

def query_cancel(button):
    if button == None:
        options()




#Gives users a menu screen with a list of options that the code can peform.
def options():
    user_options=easygui.buttonbox("""
    Takeaway Menu
    Options:
    1: View The Menu
    2: Add A Combo To The Menu
    3: Remove A Combo From The Menu
    4: Search The Menu
    5: Quit the program
    """, choices =["1","2","3","4","5"])
    return(user_options)


def add():
    while True:
        #Starts empty dictionairy, and asks users for the name of combo and its items.
        #It then splits these entered items into a list.
        new_combo={}
        name=easygui.enterbox("What is the Combo Called? ")
        query_cancel(name)

        #Checks that the name isnt already on the menu.
        on_menu = check(menu,name)
        if on_menu =="y":
            easygui.msgbox("That combo is already on the menu? Think of a new name.")

        else:
            items=easygui.enterbox("""List the items that you would like to include in the combo:
            (Seperate each item with a comma like so: Burger, Fries, Drink)
            Please do not enter the same item twice""")
            query_cancel(items)
            list_of_items=items.split(",")

            #Iterates through a list of items, and asks the user for the price of each item.
            #It then adds the item and its price to the empty dictionary: new_combo
            for item in list_of_items:
                price = easygui.enterbox(f"What is the price of {item} (Do not enter: $5, instead enter 5 or 5.5)")
                query_cancel(price)
                new_combo[item] = price

            #Calls the display function allowing new combo to be displayed in easygui.
            #User is then asked to check whether the new combo is correct.
            adding = "adding"
            new_com = display(new_combo)
            user_choice = easygui.buttonbox(f"{new_com} \n Are these items and prices correct?", choices = ["Yes","No"])

            if user_choice == "No":
                user_choice = easygui.buttonbox("Would you still like to add the combo meal to the menu anyway?", choices = ["Yes","No"])
                if user_choice == "No":
                    easygui.msgbox(f"{name} has been removed from the menu.")

                    break

            menu[name] = new_combo
            easygui.msgbox(f"{name} has been added to the menu.")
            break


#Formats a dictionary created through a for loop, so that it can be printed using easygui.
#Is used for viewing the menu, and adding to it.
def display(dictionary):
    display_string = ""
    for key, item in dictionary.items():
        display_string += (f"{key} : ${item} \n")
    return(display_string)



def output_menu(menu):
    output = ""
    for combo_name,combo_info in menu.items():
        output +=f"\n{combo_name.upper()}:\n"
        for key in combo_info:
            price = (combo_info[key])
            output += f"\t {key} : ${price}\n"
    print(output)
    easygui.msgbox(f"Here is the menu: \n {output}")
    



#Checks whether a variable (key) is already a key within a dictionary.
def check(menu,key_name):
    on_menu = "n"
    if key_name in menu.keys():
        on_menu = "y"
        return(on_menu)


#Asks users to remove a combo meal from menu. User inputs which combo they want to remove.
#The program calls the function check, to check whether this combo is on the menu.
#if it is then the combo is deleted, else the user has to re-enter a combo_name.
def remove(menu,combo_name,):
    while True:
            combo_name = easygui.enterbox("What combo meal would you like to remove from the menu?")
            query_cancel(combo_name)
            on_menu = check(menu,combo_name)
            if on_menu == "y":
                easygui.msgbox(f"The combo '{combo_name} has been deleted from the menu")

                del menu[combo_name]
                print(menu)
                break
            else:
                easygui.msgbox(f"The combo meal: {combo_name}, is not on the menu.")



def search(menu):
        combo_name = easygui.enterbox("What combo meal would you like to search the menu for?")
        query_cancel(combo_name)
        on_menu = check(menu,combo_name)

        if on_menu == "y":
            #!!! TOLD BY TEACHER THAT DELETE WAS ONLY CHANGE WE SHOULD DO!!!
            user_choice = easygui.buttonbox(f" Here is the combo meal you searched for: {menu[combo_name]}. Would you like to make any changes to the combo_menu?",
                                                choices = ["No","Delete From Menu"])
            if user_choice == "Delete From Menu":
                del menu[combo_name]
                print(menu)
        else:
            easygui.msgbox(f"The combo: '{combo_name}' doesn't exist.")


#Takes the user back to the main menu after going through a functio and allows them to quit.
while True:
    #Calls options function, displays options to user,
    #Then the user selects the thing they want the program to do and stores this as user_option.
    user_option = options()

    #Based on what option the user selects, the program calls the function related to the option.
    if user_option == "1":
        output_menu(menu)
        

    elif user_option == "2":
        add()

    elif user_option == "3":
        combo_name = ""
        remove(menu,combo_name,)

    elif user_option == "4":
        search(menu)

    elif user_option == "5":
        break
quit