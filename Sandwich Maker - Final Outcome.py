"""Sandwich Maker - Final Outcome"""
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
    meats = []
    garnishes = []
    total_price = 0.0
    while choice != "xxx":
        order_summary = (
            f"Your order currently costs ${total_price:.2f}, and "
            f"consists of:\n\n"
            f"Bread - {bread}\n"
            f"Meat - {', '.join(meats)}\n"
            f"Garnishes - {', '.join(garnishes)}\n\n"
            f"What would you like to select/change?"
        )
        choice = easygui.buttonbox(order_summary, "MAIN MENU",
                                   choices=("Select Bread", "Select Meat",
                                            "Select Garnishes", "Prices",
                                            "Finish", "Quit"))
        if choice == "Select Bread":
            selected_bread = select_bread()
            total_price -= round(get_item_price("Bread", bread), 2)
            bread = selected_bread
            total_price += round(get_item_price("Bread", selected_bread), 2)
        elif choice == "Select Meat":
            selected_meats = select_meat()
            total_price -= sum([get_item_price("Meat", meat) for meat in meats])
            meats = selected_meats
            total_price += sum([get_item_price("Meat", meat) for meat in selected_meats])
        elif choice == "Select Garnishes":
            selected_garnishes = select_garnish()
            total_price -= sum([get_item_price("Garnish", garnish) for garnish in garnishes])
            garnishes = selected_garnishes
            total_price += sum([get_item_price("Garnish", garnish) for garnish in selected_garnishes])
        elif choice == "Prices":
            prices()
        elif choice == "Finish":
            if not (bread and meats and garnishes):
                easygui.msgbox("Please select at least one bread, one meat, and one garnish before finishing.", "Error")
            else:
                final_order_summary = (
                    f"Your final order costs ${total_price:.2f}, and "
                    f"consists of:\n\n"
                    f"Bread - {bread}\n"
                    f"Meat - {', '.join(meats)}\n"
                    f"Garnishes - {', '.join(garnishes)}"
                )
                easygui.msgbox(final_order_summary)
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
    formatted_prices = "\n".join([f"{item}: ${price:.2f}" for item_dict in
                                  prices_list for item, price in
                                  item_dict.items()])
    easygui.msgbox(formatted_prices, f"{category} Prices")


def get_item_price(category, item):
    for menu_item in MENU.get(category, []):
        if item in menu_item:
            return menu_item[item]
    return 0.0  # Return 0 if the item is not found (for error handling)


def confirm_quit():
    confirm = easygui.buttonbox("Please confirm that you would like to quit "
                                "the program.", "Confirm Quit",
                                choices=("Yes - Quit", "No - Main Menu"))
    if confirm == "Yes - Quit":
        exit()
    else:
        main_menu()


# Main...
easygui.msgbox("Hello! Welcome to the online Sandwich Store!", "MAIN MENU")
main_menu()
