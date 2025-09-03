# Class Attribute v/s Object Attribute
# Class Attribute: Shared by all instances of the class
# Object Attribute: Unique to each instance of the class

class human:
    # Class Attribute
    country = "indian"

    def __init__(self, name, age):
        # Object Attribute
        self.name = name
        self.age = age
        # This will create an object attribute with the same name as the class attribute
        self.state = "bihari"


najru = human("najru", 22)  # Creating an object of the class human
print(najru.country)  # Accessing class attribute using object
print(najru.state)  # Accessing object attribute using object
print(najru.name)  # Accessing object attribute using object
print(najru.age)  # Accessing object attribute using object
