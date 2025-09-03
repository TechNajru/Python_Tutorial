# Magic Methods ( __init__)
# Magic methods are special methods in Python that start and end with double underscores (dunder).
# They allow you to define the behavior of objects in a class, such as initialization, representation, and arithmetic operations.
# Magic methods are also known as dunder methods (double underscore methods).

class human:
    def __init__(self):
        print("human object created")


richa = human()
najrudeen = human()
india = human()


# The __init__ method is called when an object of the class is created.
# It is used to initialize the attributes of the object and perform any setup required for the object.
# The __init__ method is a constructor in Python, and it is called automatically when an object is created.
# It can take parameters to initialize the object's attributes.

class human:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def eat(self):
        print("Eating...")


najrudeen = human("Najrudeen", 25)
richa = human("Richa", 30)
india = human("India", 28)

print(najrudeen.age)
print(richa.name, richa.age)
print(india.age)

print(najrudeen.name, najrudeen.age)

# __init__ method


class human:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def name_age(self):
        print(f"name & age: {self.name} & {self.age}")

    def change_age(self, new_age):
        self.age = new_age


najrudeen = human("Najrudeen", 25)
richa = human("Richa", 30)
india = human("India", 28)

najrudeen.change_age(26)
richa.change_age(31)

print(najrudeen.age)  # Output: 26
print(richa.age)  # Output: 31


india.name_age()
richa.name_age()
najrudeen.name_age()


najrudeen.profession = "Software Engineer"
richa.profession = "Data Scientist"

print(najrudeen.profession)  # Output: Software Engineer
print(richa.profession)  # Output: Data Scientist
