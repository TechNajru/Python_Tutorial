# Comprehension

students = [(97, 97, 89, 67, 56, 23, 19, 50)]
new_list = [x[0] for x in students]
print(students)

# by using Comprehension (list condition)

list1 = [x for x in students if x[1] > 80]
print(list1)
