# While Loop

num = 1
while num <= 5:
    print(num)
    num = num + 1
print("while loop ends")

# Even Number b/w 1 to 10
num = 2
while num <= 10:
    if num % 2 == 0:
        print(num)
    num = num + 1
print("loop ends")

# Guess Attempt game

num = 50
guess = 0
attempt = 0
while guess != num:
    guess = int(input("guess a number"))
    attempt += 1
print(f"you guess it right in {attempt} attempts")
