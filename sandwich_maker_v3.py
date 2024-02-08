"""Sandwich Maker - Version 3"""
# Imports...
import easygui

# Lists...
MENU = {
    "Bread": [
        {"Wholemeal": 1.00},
        {"White": 0.80},
        {"Cheesy White": 1.20},
        {"Gluten Free": 1.40}
    ],
    "Meat": [
        {"Chicken": 2.69},
        {"Beef": 3.0},
        {"Salami": 4.0},
        {"Vegan Slice": 3.3}
    ],
    "Garnish": [
        {"Onion": 1.69},
        {"Tomato": 1.0},
        {"Lettuce": 2.0},
        {"Cheese": 2.5}
    ]
}

# Functions...


def main_menu():
    bread = select_bread()
    meats = select_meat()
    garnishes = select_garnish


def select_bread():
    choice = easygui.buttonbox("Please select a bread option:",
                               "Choose Your Bread",
                               choices=("Wholemeal", "White",
                                        "Cheesy White",
                                        "Gluten Free", "Quit"))
    if choice == "Quit":
        confirm_quit()
    return choice


def select_meat():
    num_meat = easygui.buttonbox("How many meats do you want in your "
                                 "sandwich?", "Num Meats",
                                 choices=(1, 2, 3, 4, "Quit"))
    if num_meat == "Quit":
        confirm_quit()
    elif num_meat == 1:
        meat_1 = easygui.buttonbox("Please select your meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
    elif num_meat == 2:
        meat_1 = easygui.buttonbox("Please select your first meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
        meat_2 = easygui.buttonbox("Please select your second meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
    elif num_meat == 3:
        meat_1 = easygui.buttonbox("Please select your first meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
        meat_2 = easygui.buttonbox("Please select your second meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
        meat_3 = easygui.buttonbox("Please select your third meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
    else:
        meat_1 = easygui.buttonbox("Please select your first meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
        meat_2 = easygui.buttonbox("Please select your second meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
        meat_3 = easygui.buttonbox("Please select your third meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
        meat_4 = easygui.buttonbox("Please select your fourth meat option:",
                                   "Choose Your Meat",
                                   choices=("Chicken", "Beef", "Salami",
                                            "Vegan Slice", "Quit"))
    meat_choices = [meat_1, meat_2, meat_3, meat_4]
    return meat_choices



def select_garnish():
    return


def prices():
    choice = ""
    while choice != "Return":
        choice = easygui.buttonbox("What prices would you like to view?",
                                   "Prices",
                                   choices=("Breads", "Meats",
                                            "Garnishes", "Return"))
        if choice == "Breads":
            easygui.msgbox()
        elif choice == "Meats":
            easygui.msgbox()
        elif choice == "Garnishes":
            easygui.msgbox()
        else:
            return


def confirm_quit():
    confirm = easygui.buttonbox("Please confirm that you would like to quit "
                                "the program.", "Confirm Quit",
                                choices=("Yes - Quit", "No - Return"))
    if confirm == "Yes - Quit":
        exit()
    else:
        return

# Main...


easygui.msgbox("Hello! Welcome to the online Sandwich Store!", "MAIN MENU")
main_menu()
