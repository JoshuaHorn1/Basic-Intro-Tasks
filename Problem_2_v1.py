"""Basic Test Problem 2 - Version 1"""
fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]
for item in fish:
    print(item[0])
    print()
for item in fish:
    print(item[0], item[1], item[2])
    print()
print(f"The longest word in the list 'fish' is {max(fish)}")
print()
items_with_space = [item for item in fish if ' ' in item]
print(f"Items in the list with a space are: {items_with_space}")
items_with_cod = [item for item in fish if 'cod' in item]
print(f"Item's in the list containing 'cod' are: {items_with_cod}")
