# map function

students = [("najru,90", ("richa,78"), ("india,46"))]

names = []

for x in students:
    names.append(x[0])
print(names)

# By using Lambda function

names = list(map(lambda x: x[1], students))
print(names)
