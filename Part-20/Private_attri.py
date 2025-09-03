# Private Attributes
# Private attributes are not accessible from outside the class.
# To create a private attribute, add two underscores before the attribute name.
# Example:

class human:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        print(self.__name)

    def get_age(self):
        print(self.__age)


najru = human("Najru", 22)

najru.get_name()
najru.get_age()
