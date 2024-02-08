import easygui

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
        meat = easygui.buttonbox(f"Please select your {ordinal_number(i + 1)} meat option:",
                                  "Choose Your Meat",
                                  choices=("Chicken", "Beef", "Salami", "Vegan Slice", "Quit"))
        if meat == "Quit":
            confirm_quit()
            return
        meat_choices.append(meat)

    return meat_choices

def ordinal_number(n):
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    return f"{n}{suffixes.get(n, 'th')}"

def confirm_quit():
    # Implement your confirmation logic here
    print("Quitting the program.")

# Example usage:
meats_selected = select_meat()
print("Selected meats:", meats_selected)
