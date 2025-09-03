# Function is any thing by which a operation is performed or happen

def say_hello():
    print("hii")
    print("good morning")


print("function created")

say_hello()
say_hello()

# Table of 2


def table_2():
    for num in range(1, 11):
        print(f"2*{num}= {2*num}")


table_2()


def star_pattern():
    for x in range(1, 6):
        for y in range(1, x+1):
            print("*", end="")
        print("")


star_pattern()
star_pattern()
table_2()
say_hello()