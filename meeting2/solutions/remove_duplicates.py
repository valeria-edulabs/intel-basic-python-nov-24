# Exercise:
# Write a function remove_duplicates that takes a list of integers as input and returns
# a new list with all duplicate values removed, keeping only the first occurrence of each number in the original list.

# Requirements:
#
# Use a loop to iterate over the list and keep track of the numbers that have already been encountered
# (you can use an additional list to store those).
# Return a list without any duplicates, maintaining the order of the original list.


# Usage:
# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
# print(remove_duplicates([10, 10, 10, 1, 2, 3]))  # Output: [10, 1, 2, 3]
# print(remove_duplicates([1, 1, 1, 1]))            # Output: [1]
# print(remove_duplicates([]))                       # Output: []


def remove_duplicates(lst):
    # Create an empty list to store unique numbers
    unique_list = []

    # Iterate over each number in the input list
    for num in lst:
        # Add the number to the unique_list if it hasn't been added already
        if num not in unique_list:
            unique_list.append(num)

    return unique_list
