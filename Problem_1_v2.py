"""Basic Problem Task 1 - Version 2"""


def get_code():
    user_input = input("Enter your secret 4-digit pin: ")
    while len(str(user_input)) != 4 and not user_input.isalnum():
        if user_input.isalpha():
            print("Sorry, the secret code must contain only numbers. ")
        else:
            print("Sorry, the secret code must contain only numbers. ")
    return user_input


code = get_code()
print(f"Your code is {code}.")
