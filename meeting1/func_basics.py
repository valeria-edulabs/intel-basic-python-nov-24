def get_age():
    name = input("Insert your name: ")
    year = input("Year: ")
    age = 2024 - int(year)
    print(f"Hi {name}, You are {age} years old")
    return age

ret_val = get_age()
print("retrun val", ret_val)



# print("dddd")
# input("insert somwthing")