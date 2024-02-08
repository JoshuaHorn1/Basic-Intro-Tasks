"""Basic Practice Task 6 - Version 1"""


def find_largest_item(my_list):
    if not my_list:
        return None
    largest_item = my_list[0]
    for item in my_list:
        if item > largest_item:
            largest_item = item
    return largest_item


numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]
largest_number = find_largest_item(numbers)
print(f"The largest item in the list is: {largest_number}")
