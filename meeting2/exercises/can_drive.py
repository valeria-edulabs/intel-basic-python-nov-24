# Exercise:

# Write a function can_drive that takes two arguments:
# drink (a string representing the alcoholic drink, e.g., "beer", "wine", "whiskey")
# and amount_ml (an integer representing the amount of drink consumed in milliliters).
# The function should return True if it is legally allowed to drive,
# and False if you cannot drive based on the following legal limits:
#
# Beer: 500 ml (1 regular portion)
# Wine: 200 ml (1 regular portion)
# Whiskey: 50 ml (1 regular portion)

# If the amount consumed exceeds the legal portion for that drink type, return False.
# If the amount consumed is within the legal limit, return True.
# If no alcohol was consumed (drink == "none"), return True.

# Usage
# print(can_drive("beer", 500))      # Output: True
# print(can_drive("beer", 600))      # Output: False
# print(can_drive("wine", 200))      # Output: True
# print(can_drive("whiskey", 30))    # Output: True
# print(can_drive("whiskey", 60))    # Output: False
# print(can_drive("none", 0))        # Output: True


# Advanced:
# Write a function that takes list of drinks, and list of corresponding amounts.