# *args mean you can pass ultimate arguments

def add(*num):
    result = 0
    for n in num:
        result = result + 1
    print(result)


add(2, 3, 4)
