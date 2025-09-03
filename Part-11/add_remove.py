# Adding  items in list

names = ["Najru", "india", "viraj", "a", 1, 2, 3]
names.append("richa")
print(names)

names.insert(2, "Tarun")
print(names)

# removing items in list

names.pop()
names.pop()
print(names)

names.pop(3)
print(names)

names.remove("Najru")
print(names)


del names[2:6]
print(names)

names.clear()
print(names)
