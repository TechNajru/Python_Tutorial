# tuples are same as list but difference is they are immutable
# tuples are defined by ()
# tuples are used to store multiple items in a single variable
# tuples are ordered, unchangeable, and allow duplicate values
# tuples are faster than lists

student = ("Najru", 1, 2, 7, 6,)
print(student)
print(type(student))

# creating a tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# creating a tuple with one item
my_tuple = ("apple",)
print(my_tuple)

# creating a tuple with different data types
my_tuple = ("apple", 1, 2.5, True)
print(my_tuple)

# creating a tuple with a list
my_list = ["apple", "banana", "cherry"]
my_tuple = tuple(my_list)
print(my_tuple)

student = ()
print(student)

student = "najrudeen", "varun", "tarun ", "richa"
print(student)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1+t2
print(t3)

t3 = t2*2
print(t3)

tuple1 = (1, 2, 3, 4, 5)
a = tuple1[0]
b = tuple1[-2]
print(a)
print(b)

tuple1 = (1, 2, 3, 4)
x, y, z, t = tuple1
print(y)
print(t)

if 3 in tuple1:
    print("yes")
else:
    print("no")
