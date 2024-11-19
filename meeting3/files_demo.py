file_handler = open("data/alice_in_wonderland.txt", "r", encoding="utf-8")
print(file_handler)
content = file_handler.read()
print(len(content), content[:100])