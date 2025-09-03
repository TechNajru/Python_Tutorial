# Variable Concept
# Types of Variable in Python

num = 1  # Global Variable


def hello():
    message = "good"  # Local Variable
    print(num)


hello()
# print(message)


# Local Variable are call only in function and can't be call globally

# Global variable can call globally means call everywhere

# Arguments are local variable can't call outside the function


var0 = "global variable"


def fun1():
    var0 = "local variable"
    print(var0)


fun1()
print(var0)


# Error show because local variable is accessed only where you create (in function) can't use in another function

var = "global variable"


def fun():
    var1 = "local variable 1"


def fun1():
    var2 = "local variable 2"
    print(var1)


fun1()
