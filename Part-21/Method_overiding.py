# Method Overriding
# Method overriding is a feature in object-oriented programming that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
# When a method in a subclass has the same name, same parameters, and same return type as a method in its superclass, the method in the subclass overrides the method in the superclass. This allows the subclass to provide its own behavior for that method while still inheriting the properties and methods of the superclass.
# Method overriding is a powerful feature that allows for dynamic polymorphism, where the method that gets executed is determined at runtime based on the object type.
# This allows for more flexible and reusable code, as subclasses can customize the behavior of inherited methods without modifying the superclass.
# In Python, method overriding is achieved by defining a method in the subclass with the same name as the method in the superclass. When the method is called on an instance of the subclass, the subclass's implementation is executed instead of the superclass's implementation.
# Method overriding is a key concept in object-oriented programming that allows for more flexible and reusable code. It enables subclasses to customize the behavior of inherited methods without modifying the superclass, leading to dynamic polymorphism and better code organization.

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


class teacher(uni_person):
    def make_attendance(self):
        print("Attendance is made by teacher")

    def leave_application(self):
        print("Leave application is submitted wait for HOD approval")

    def upload_test(self):
        print("Test is uploaded by teacher")


class students(uni_person):
    def upload_answer(self):
        print("Answer is uploaded by student")


class clerk(uni_person):
    def upload_data(self):
        print("data are uploaded by clerk")


najru = students("Najrudeen", 21)
najru.leave_application()

richa = teacher("Richa", 22)
richa.leave_application()

print("")
# Method Overloading


class Smart_teacher(uni_person):
    def leave_application(self):
        super().leave_application()
        print("& waiting for HOD approval")


richa = Smart_teacher("Richa", 22)
richa.leave_application()

print("")


najrudeen = students("Najrudeen", 21)
najrudeen.leave_application()
