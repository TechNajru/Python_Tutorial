# unpacking a list

names = ["Najru", "india", "viraj"]
first, second, third = names

print(first)
print(second)
print(third)

names = ["Najru", "india", "viraj", "a", 1, 2, 3]
first, second, third, *list2 = names

print(first)
print(second)
print(third)
print(list2)

