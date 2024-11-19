# Exercise:
# Write a function format_full_name that takes two arguments, first_name and last_name,
# and returns a formatted full name. The function should:
#
# Capitalize the first letter of each name and make the rest lowercase.
# Handle cases where either first_name or last_name is missing by
# returning only the name that is provided (or an empty string if both are missing).

# Usage
# print(format_full_name("jOhN", "DOE"))  # Output: "John Doe"
# print(format_full_name("ALICE", ""))    # Output: "Alice"
# print(format_full_name("", "SMITH"))    # Output: "Smith"
# print(format_full_name("", ""))         # Output: ""


def format_full_name(first_name=None, last_name=None):
    # Capitalize and format each name if provided
    first_name = first_name.capitalize() if first_name else ""
    last_name = last_name.capitalize() if last_name else ""

    # Check different cases for missing names
    if first_name and last_name:
        return f"{first_name} {last_name}"
    elif first_name:
        return first_name
    elif last_name:
        return last_name
    else:
        return ""



