name = "Valeria"

def convert_bytes_to_kb(num_bytes):
    global name
    print(name)
    name = "Yogev"
    print(name)
    kb = num_bytes / 1024
    return kb


b = input("Bytes: ")
kb = convert_bytes_to_kb(int(b))
print(f"KB: {kb}")
print(name)

