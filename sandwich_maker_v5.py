"""Sandwich Maker - Version 5"""
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
            garnishes = select_garnish()
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
                                 "sandwich?", "Number Of Meats",
                                 choices=list(range(1, max_meats + 1)) +
                                         ["Quit"])
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


def select_garnish():
    max_garnishes = 4
    garnish_choices = []
    num_garnishes = easygui.buttonbox("How many garnishes do you want in your "
                                      "sandwich?",
                                      "Number Of Garnishes",
                                      choices=
                                      list(range(1, max_garnishes + 1)) +
                                      ["Quit"])
    if num_garnishes == "Quit":
        confirm_quit()
        return
    for i in range(num_garnishes):
        garnish = easygui.buttonbox(f"Please select your "
                                    f"{ordinal_number(i + 1)} garnish option:",
                                    "Choose Your Garnish",
                                    choices=("Onion", "Tomato", "Lettuce",
                                             "Cheese", "Quit"))
        if garnish == "Quit":
            confirm_quit()
            return
        garnish_choices.append(garnish)
    return garnish_choices


def ordinal_number(n):
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    return f"{n}{suffixes.get(n, 'th')}"


def prices():
    choice = ""
    while choice != "Return":
        choice = easygui.buttonbox("What prices would you like to view?",
                                   "Prices",
                                   choices=("Breads", "Meats",
                                            "Garnishes", "Return"))
        if choice == "Breads":
            display_prices("Bread")
        elif choice == "Meats":
            display_prices("Meat")
        elif choice == "Garnishes":
            display_prices("Garnish")
        else:
            return


def display_prices(category):
    prices_list = MENU.get(category, [])
    formatted_prices = "\n".join([f"{item}: ${price}" for item_dict in prices_list for item, price in item_dict.items()])
    easygui.msgbox(formatted_prices, f"{category} Prices")


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
