"""Sandwich Maker - Version 1
Created the menu list, and some of the primary base functions."""
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
    easygui.msgbox("Hello! Welcome to the online Sandwich Store!", "MAIN MENU")
    bread = select_bread()
    meats = select_meat()
    garnishes = select_garnish


def select_bread():
    choice = easygui.buttonbox("Please select a bread option:",
                                     "Choose Your Bread",
                                     choices=("Wholemeal", "White",
                                              "Cheesy White", "Gluten Free"))
    return choice


def select_meat():
    num_meat = easygui.buttonbox("Please select one or more meat options:",
                                 "Choose Your Meat",
                                 choices=("Chicken", "Beef", "Salami",
                                          "Vegan Slice", "View Prices"))

def select_garnish():


def prices():
    easygui.buttonbox("What prices would you like to view?", "Prices")



# Main...

main_menu()
