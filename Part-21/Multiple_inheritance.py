# multiple-level inheritance

class animal:
    def eat(self):
        print("Eating...")


class bird:
    def fly(self):
        print("Flying...")


class eagle(animal, bird):
    def breed(self):
        print("white-tailed eagle")


e = eagle()
e.eat()  # Inherited from animal class
e.fly()  # Inherited from bird class
e.breed()  # Inherited from eagle class
