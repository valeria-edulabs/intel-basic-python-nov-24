# animals = ["elephant", "zebra", "cat", "dog"]
# for animal in animals:
#     print(animal, len(animal))

my_range = range(10)
print(type(my_range))
for i in my_range:
    print(i)

big_range = range(346, 1_000_000, 56)
print(7485 in big_range)


print(my_range)


drinks = ["beer", "wine", "water"]
amounts = [500, 200, 1000]

for i in range(len(drinks)):
    curr_drink = drinks[i]
    curr_amount = amounts[i]
    print(f"{curr_drink}: {curr_amount}")


temp = (4,5,6,7,8)

for d, a in zip(drinks, amounts):
    print(f"{d}: {a}")

for d, a, t in zip(drinks, amounts, temp):
    print(f"{d}: {a}", t)

for d in drinks:
    pass

for char in "Apple":
    pass

sentence = "The sky is blue"
for word in sentence.split():
    print(word)
