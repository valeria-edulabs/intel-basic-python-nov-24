# names_list = []
# name = ""
# while name != "$":
#     name = input("Insert a name: ")
#     names_list.append(name)
# names_list.pop()
# print("The names are:", names_list)
# print("Total names inserted:", len(names_list))
# total_chars = sum([len(word) for word in names_list])
# chars = []
# for word in names_list:
#     chars.append(len(word))
# print("Total characters: ", total_chars)


names_list = []
while True:
    name = input("Insert a name: ")
    if name == "Dont know":
        print("bla")
        continue
    if name != "$":
        names_list.append(name)
    else:
        break

print("The names are:", names_list)
print("Total names inserted:", len(names_list))
total_chars = sum([len(word) for word in names_list])