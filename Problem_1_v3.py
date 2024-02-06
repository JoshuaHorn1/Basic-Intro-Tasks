"""Basic Problem Task 1 - Version 3"""


def get_code():
    user_input = input("Enter your secret 4-digit pin: ")
    while len(user_input) != 4 or not user_input.isdigit():
        print("Sorry, the secret code must be exactly four digits and contain only numbers.")
        user_input = input("Enter your secret 4-digit pin: ")
    return int(user_input)


code = get_code()
print(f"Your code is {code}.")
