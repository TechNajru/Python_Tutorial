print("legal age of marriage in India")
gender = input("Enter male (m) or female (f)")
age = int(input("enter age"))

if gender == "m":
    if age >= 24:
        print("legal age of marriage")
    else:
        print("not a legal age of marriage")
elif gender == "f":
    if age >= 21:
        print("legal age of marriage")
    else:
        print("child marriage")
else:
    print("enter m for male or f for female")
