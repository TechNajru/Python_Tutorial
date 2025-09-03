# Explicit type Conversion (Manual)

data = 5            # int
da = type(data)
print(da)

data = 2.5  # float
data1 = "hello"  # str
data2 = True  # bool
data3 = "False"  # str
data4 = "4"  # str

data = "1"
result = data + "1"      # if we add only 1 without quotation it shows error
print(result)

data = "1"
result = int(data) + 1
print(result)


# Use Following Keyword to change data types

# int()
# float()
# str()
# bool()


#  "", 0, None is equal to False else True

data = 0
data = bool(data)
print(type(data))
print(data)


data7 = "False"
data7 = bool(data7)
print(data7)


# Implicit Type Conversion (Automatically)

x = 5                 # 5 (int) automatically converted into 5.0 (float)
y = 2.5
sum = x+y
print(sum)


x = 5
y = 2
result = x/y
print(result)
print(type(result))


# Comparison Operator

print(3 > 10)
print(6 <= 6)
print(2 == 2)
x = 6
print(x == 8)
print("apple" > "aball")  # ascii value comparison b=98 and p=113
