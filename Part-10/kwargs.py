# **kwargs is work same as *args in multiple times

def add_student(**args):
    for x, y in args.items():
        print(f"{x} = {y}")


add_student(name="najrudeen", roll=37)

add_student(name="richa", age=22)
