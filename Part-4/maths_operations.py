import math  # math is a python library
num1 = 5
num2 = 2.5

result = num1 + num2
print(result)

result = num1 - num2
print(result)

result = num1 * num2
print(result)

result = num1 / num2
print(result)

num1 = 5
num2 = 2
result = num1 / num2       # Result in Floating Point
print(result)

result = num1 // num2      # Result in Integer Value, Use // for integer value result
print(result)

result = num1 ** num2      # ** is used for power value
print(result)

result = 2**3              # 2^3 = 8
print(result)

result = num1 % num2
print(result)              # % is used to reminder find

num1 += 8                  # Add 8 to num1(5), 8+5=13
print(num1)

num1 = 2.4
num2 = 2.5
num3 = 2.9
print(round(num1))         # Round up the value to higher one or lower one
print(round(num2))
print(round(num3))

num4 = -2.5
num5 = -3.6
print(abs(num4))          # change sign and value from negative to positive
print(abs(num5))

num1 = 2.5
num2 = 2.9
num3 = 2.0
num4 = 2.05
result = math.ceil(num1)  # 2.0 ke upper ko 3 kardega
print(result)

result = math.ceil(num2)
print(result)

result = math.ceil(num3)
print(result)

result = math.ceil(num4)
print(result)

num5 = 2.99
num6 = 2.05
result = math.floor(num5)  # 2.0 se niche ko 2 kr dega
print(result)

result = math.floor(num6)
print(result)
