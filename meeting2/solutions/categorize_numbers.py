# Exercise:
# Write a function categorize_numbers that takes a list of integers and returns a
# tuple of three lists: positives, negatives, and zero.

numbers = [10, -3, 0, 5, -7, 0, 2]

# Usage:
# print(categorize_numbers(numbers))
# # Output: ([10, 5, 2], [-3, -7], [0, 0])


def categorize_numbers(numbers):
    # Initialize the dictionary with empty lists for each category
    categories = {
        "positive": [],
        "negative": [],
        "zero": []
    }

    # Iterate over each number in the input list
    for number in numbers:
        # Use if/elif/else to categorize the number
        if number > 0:
            categories["positive"].append(number)
        elif number < 0:
            categories["negative"].append(number)
        else:
            categories["zero"].append(number)

    return categories
