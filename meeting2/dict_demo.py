months = {
    1: "January",
    2: "February",
    3: "March"
}

print(months[2])


cities = {
    "Israel": "Jerusalem",
    "US": "Washington",
    "France": "Paris"
}
print(cities["Israel"])
cities["Australia"] = "Canberra"

cities["France"] = "blabla"
print(cities)

countries = {
    "Israel": {
        "capital": "Jerusalem",
        "population": 10_000_000,
        "languages": ["Hebrew", "Arabic", "English"]
    },
    "US": {
        "capital": "Washington",
        "population": 350_000_000,
        "languages": ["English"]
    },
    "France": {
        "capital": "Paris",
        "population": 45_000_000,
        "languages": ["French"]
    }
}


print(countries["France"]["languages"])
print(countries["Israel"]["languages"][-1])
print("Germany" in countries)