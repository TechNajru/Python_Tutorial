# Break Statement

for x in range(10):
    if x == 5:
        break
    print(x)
print("end of loop")


# Break Usage

x = 1
while x <= 20:
    if x == 10:
        break
    print(x)
    x = x+1


# GUESS ATTEMPT GAME

print("to quit press 0")
num = 50
guess = 0
attempt = 0
while True:
    guess = int(input("guess a no."))
    if guess == 0:
        print("you loose")
        break
    attempt += 1
    if guess == num:
        print(f"you won in {attempt} attempts")
        break
print("i hope you enjoy game")
