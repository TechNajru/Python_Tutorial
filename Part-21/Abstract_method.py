# Abstract Methods
# Abstract methods are methods that are declared but contain no implementation.
# They are used to define a common interface for all subclasses of an abstract class.
# Abstract classes cannot be instantiated, and they are meant to be subclassed.
# Abstract methods are defined using the @abstractmethod decorator from the abc module.
# The abc module provides the ABC class, which is the base class for defining abstract classes.
# Abstract classes can contain both abstract methods and concrete methods (methods with implementation).
# Subclasses of an abstract class must implement all abstract methods in order to be instantiated.

from abc import ABC, abstractmethod


class animal:
    def eat(self):
        print("eating...")


class bird(animal):
    def fly(self):
        print("flying...")


class fish(animal):
    def swim(self):
        print("swimming")

    def die(self):
        print("fish die on water")


f = fish()
f.die()
