# jab bhi kisi function ke ander kuch return nhi karta tab wo None return karta hai

def return_add(num1, num2):
    result = num1 + num2
    return result


r = return_add(2, 8)
print(r)

r = return_add(23, 56)
print(r)


# return usage

def return_two(num1, num2):
    r1 = num1 * 2
    r2 = num2 * 3
    return r1, r2


print(return_two(2, 5))

return_two(4, 8)
res1, res2 = return_two(2, 6)
print(res1)
print(res2)
