# Filter Function

students = [(97, 97, 89, 67, 56, 23, 19, 50)]
new_list = []

for x in students:
    if x[1] > 90:
        new_list.append(x)
print(new_list)


# by using filter  function
new_list = filter(lambda x: x[1] >= 90, students)
new_list = list(new_list)
print(new_list)
