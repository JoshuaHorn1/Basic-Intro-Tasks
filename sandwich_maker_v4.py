"""Sandwich Maker - Version 4
Condensed and improved the meat choice algorithm"""
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
    choice = ""
    bread = ""
    meats = ""
    garnishes = ""
    while choice != "xxx":
        choice = easygui.buttonbox("Your order currently costs $_, and "
                                   "consists of:\n\n"
                                   f"Bread - {bread}\n"
                                   f"Meat - {meats}\n"
                                   f"Garnishes - {garnishes}\n\n"
                                   f"What would you like to select/change?",
                                   "MAIN MENU",
                                   choices=("Select Bread", "Select Meat",
                                            "Select Garnishes", "Finish",
                                            "Quit"))
        if choice == "Select Bread":
            bread = select_bread()
        elif choice == "Select Meat":
            meats = select_meat()
        elif choice == "Select Garnishes":
            garnishes = select_garnish
        elif choice == "Finish":
            easygui.msgbox("Your final order costs $_, and consists of:\n\n"
                           f"Bread - {bread}\n"
                           f"Meat - {meats}\n"
                           f"Garnishes - {garnishes}")
            quit()
        else:
            confirm_quit()


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
    max_meats = 4
    meat_choices = []

    num_meat = easygui.buttonbox("How many meats do you want in your "
                                 "sandwich?", "Num Meats",
                                 choices=list(range(1, max_meats + 1)) + ["Quit"])
    if num_meat == "Quit":
        confirm_quit()
        return
    for i in range(num_meat):
        meat = easygui.buttonbox(f"Please select your {ordinal_number(i + 1)} "
                                 f"meat option:", "Choose Your Meat",
                                 choices=("Chicken", "Beef", "Salami",
                                          "Vegan Slice", "Quit"))
        if meat == "Quit":
            confirm_quit()
            return
        meat_choices.append(meat)
    return meat_choices


def ordinal_number(n):
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    return f"{n}{suffixes.get(n, 'th')}"


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
        main_menu()

# Main...


easygui.msgbox("Hello! Welcome to the online Sandwich Store!", "MAIN MENU")
main_menu()
