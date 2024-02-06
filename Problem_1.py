"""Simple Problem Task 1"""
# Functions...


def get_code():
    user_input = int(input("Enter your secret 4-digit pin: "))

    while len(str(user_input)) != 4:
        print("Sorry, your code must be exactly four digits in length.")
        user_input = int(input("Enter your secret 4-digit pin: "))

    return user_input


# Main...


code = get_code()
print(f"Your code is {code}.")
