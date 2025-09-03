# Range () Function returns a sequence of numbers, start from 0, increment by 1 and stops before specified number.

range(5)
range(2, 5)
range(1, 10, 2)


# For Loop

for num in range(5):
    print("Najru")
print("rohit")
print("loop end")


# even number b/w 1 to 10

for num in range(1, 11):
    if num % 2 == 0:
        print(num)


# Table of 12

for num in range(1, 11):
    print(f"12*{num}={num*12}")

# string

name = "najrudeen"
for char in name:
    print(char)

# Data Structure

cart = ["apple", "orange", "coffee"]
for item in cart:
    print(item)
