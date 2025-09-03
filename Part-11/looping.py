# looping over list

names = ["Najru", "india", "viraj", "a", 1, 2, 3]
for x in names:
    print(x)

for x, y in enumerate(names):     # return index value
    print(x, y)


# Find item in list

names = ["Najru", "india", "viraj", "a", 1, 2, 3]
p = names.index("Najru")
t = names.index("a")
print(p)
print(t)


# sorting in list

numbers = [34, 3, 45, 78, 56, 0, 67, 89, 900]
numbers.sort()
print(numbers)


numbers.sort(reverse=True)
print(numbers)

num = [8, 5, 7, 3, 90, 45, 78, 56, 89, 100]
new_list = sorted(num)
print(num)            # this will not change original list value
print(new_list)
