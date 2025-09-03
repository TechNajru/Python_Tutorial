# Inheritance in Python
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# The child class can override or extend the functionality of the parent class.
# The child class can also have its own methods and properties.
# The child class can call the parent class methods using the super() function.

class uni_person:
    def make_attendance(self):
        print("Attendance is made")

    def leave_application(self):
        print("Leave application is submitted")

    def __init__(self, name, age):
        self.name = name
        self.age = age


viraj = uni_person("Viraj", 20)
print(viraj.name)
print(viraj.age)


class teacher:
    def make_attendance(self):
        print("Attendance is made by teacher")

    def leave_application(self):
        print("Leave application is submitted by teacher")

    def upload_test(self):
        print("Test is uploaded by teacher")


class students(uni_person):
    def upload_answer(self):
        print("Answer is uploaded by student")


class clerk(uni_person):
    def upload_data(self):
        print("data are uploaded by clerk")


saurav = teacher()
print(saurav.make_attendance())
print(saurav.leave_application())
print(saurav.upload_test())

najrudeen = students("Najrudeen", 21)
print(najrudeen.name)
print(najrudeen.age)
print(najrudeen.upload_answer())


class teacher(uni_person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


richa = teacher("Richa", 22, 50000)
richa.leave_application()
print(richa.salary)
print(richa.name)
print(richa.age)
