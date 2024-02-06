"""Basic Problem Task 4 - Version 1"""
def count_character_occurrences(user_input, target_character):
    return user_input.lower().count(target_character.lower())


user_input = input("Enter a sentence: ")
target_character = input("Enter the specific character to count: ")

occurrences = count_character_occurrences(user_input, target_character)
print(f"The character '{target_character}' is used {occurrences} times in the input.")
