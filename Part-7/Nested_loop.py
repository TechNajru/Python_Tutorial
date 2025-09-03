# Nested Loop

for num in range(10):
    for num1 in range(4):
        print(f"{num},{num1}")


# Table of 12 & 15

for x in range(12, 16):
    print(f"table of {x}")
    for y in range(1, 11):
        print(f"{x}*{y}= {x*y}")


# *Star* Pattern

for x in range(1, 6):
    for y in range(1, x+1):
        print("*", end="")
    print("")


line = 1
while line <= 5:
    star = 1
    while star <= line:
        print("*", end="")
        star = star + 1
    print("")
    line = line + 1
