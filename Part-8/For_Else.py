# for_else Game

for num in range(3):
    num = int(input("enter odd no."))

    if num % 2 == 0:
        print("you loose")
    break
else:
    print("you won ")        # else tab print hoga jab loop normally end hoga without break


# LOOP end normally

x = 1
while x <= 10:
    if x == 5:
        break
    print(x)
    x = x+1 
else:
    print("loop end normally")