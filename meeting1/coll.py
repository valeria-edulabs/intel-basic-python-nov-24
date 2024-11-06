grades = [78, 90, 100, 90]
print(type(grades))
print(grades)
various = [90, 3.5, True, "abc", 98]
print(grades[0])
print(grades[2])
print(grades[-1])
print(grades[1:3])
numbers = [11,22,33,44,55,66,77,88,99]
print(numbers[3])
print(numbers[3:7])
print(numbers[3:7:2])
print(numbers[3:4])
print(numbers[3:3])
print(numbers[4:3:-1])

text = "It is November and the weather is fine"
print(text[2:6])
print(text[::-1])

words = ["It", "is", "November", "and"]
print(words[1:3])

print("hi")
print(str.lower("HELLO"))
print(text.lower())
print(text.replace("November", "January"))
print(text)
print(text.replace("is", "aaaaaaa", 1))

# print(text.split(" ")[::-1])

# text = text.split(" ")[::-1]
print(text)
print(text.lower())
print(text)
print(numbers)
print(numbers.append(1000))
print(numbers)

total = 0
for element in numbers:
    print("index", element)
    total = total + element
print(total)

for i, element in enumerate(numbers):
    print("index",i, "element", element)
    total = total + element

