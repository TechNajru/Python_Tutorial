# Multiple inheritance

class animal:
    def eat(self):
        print("Eating...")


class bird(animal):
    def fly(self):
        print("Flying...")


class eagle(bird):
    def breed(self):
        print("white-tailed eagle")


e = eagle()
e.eat()  # Inherited from animal class
e.fly()  # Inherited from bird class
e.breed()  # Inherited from eagle class
