# Accessing list Items

names = ["Najru", "india", "viraj", "a", 1, 2, 3]
marks = ["india", [90, 80, 70], [60, 67, 56], "najru", 1]

print(names[0])
print(names[2])
print(names[-1])
print(names[-5])
print(names[4])

print(marks[0])
print(marks[-2])
print(marks[3])
print(marks[2][1])

marks[1][1] = 0
print(marks[1])

print(names[8])