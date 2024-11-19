# Write a Python function categorize_birthdays_by_season(birthdays) that takes a list of dictionaries as input.
# Each dictionary represents a person and contains:
#
# "name": A string, the person's name.
# "birthday": A string in the format "YYYY-MM-DD".
# Your function should return a dictionary where the keys are seasons
# ("Spring", "Summer", "Fall", "Winter") and the values are lists of names with birthdays in those seasons.
#
# Rules for seasons:
# Winter: December 1 - February 28/29
# Spring: March 1 - May 31
# Summer: June 1 - August 31
# Fall: September 1 - November 30


birthdays = [
    {"name": "Alice", "birthday": "1990-03-15"},
    {"name": "Bob", "birthday": "1985-07-01"},
    {"name": "Charlie", "birthday": "1992-10-05"},
    {"name": "David", "birthday": "1993-09-05"},
]

# result = categorize_birthdays_by_season(birthdays)
# print(result)
# Output:
# {
#     "Winter": ["Alice"],
#     "Spring": [],
#     "Summer": ["Bob"],
#     "Fall": ["Charlie", "David"]
# }


def categorize_birthdays_by_season(birthdays):
    seasons = {
        "Winter": [],
        "Spring": [],
        "Summer": [],
        "Fall": []
    }

    for person in birthdays:
        name = person["name"]
        birthday = person["birthday"]
        month = int(birthday[5:7])

        if month in [12, 1, 2]:
            seasons["Winter"].append(name)
        elif month in [3, 4, 5]:
            seasons["Spring"].append(name)
        elif month in [6, 7, 8]:
            seasons["Summer"].append(name)
        else:
            seasons["Fall"].append(name)

    return seasons

