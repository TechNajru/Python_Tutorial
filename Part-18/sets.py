# Sets are collection of unique elements / data

list1 = [1, 2, 4, 5, 6, 2, 3, 1, 5, 3, 6]
set1 = set(list1)
print(set1)

set2 = {1, 2, 4, 7, 9, 4, 2, 6}
set2.add(90)
set2.remove(4)
print(set2)

print(len(set2))

set3 = {1, 3, 5, 4, 6, 2, 7, 8, 9, 10}
set4 = {12, 34, 56, 78, 90, 100, 3, 4, 6, 9, 10}

union = set3 | set4
print(union)

intersection = set3 & set4
print(intersection)

fruits = {"apple", "orange", "cherry"}
for x in fruits:
    print(x)

print("chrry" in fruits)
print("cherry" in fruits)

list2 = list(fruits)
print(list2)
print(list2[1])
