# Concept of oops in python
# OOPs is a programming paradigm that uses objects and classes to structure code.
# It allows for encapsulation, inheritance, and polymorphism, making code more modular and reusable.
# OOPs is widely used in Python and other programming languages to create complex applications.

class human:
    pass


najrudeen = human()

# Creating a class


class human:
    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

    def walk(self):
        print("Walking...")


najrudeen = human()
richa = human()
india = human()
viraj = human()

najrudeen.eat()
richa.sleep()
india.walk()
najrudeen.walk()
richa.eat()
