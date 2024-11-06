def convert_bytes(bytes_num, unit):
    divider = 1
    if unit == "kb":
        print("Inside if kb")
        divider = 1024
    elif unit == "mb":
        print("Inside if mb")
        divider = 1024 * 1024
    elif unit == "gb":
        print("Inside if gb")
        divider = 1024 * 1024 * 1024
    else:
        raise Exception("Invalid unit")
    print("After IF statement")
    return bytes_num / divider

print(convert_bytes(10003453, "mb"))