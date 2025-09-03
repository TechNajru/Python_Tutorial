# Lambda Function is a without name function in which many arguments are passed but only one statement is defined

student = [("najru, 98"), ("viraj,69"), ("india, 70"), ("richa,80")]
print(student)

student.sort()
print(student)


def sort_students(stu):
    return stu[1]


student.sort(key=sort_students)
print(student)

student.sort(key=lambda stu: stu[1])
print(student)
