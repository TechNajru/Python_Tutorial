# AND operator

ssc = 70
hsc = 80

if ssc >= 60 and hsc >= 70:
    print("eligible")
else:
    print("not eligible")


ssc = 50
hsc = 60

if ssc >= 60 and hsc >= 70:
    print("eligible")
else:
    print("not eligible")


# OR operators

ssc = 80
hsc = 50

if ssc >= 70 or hsc >= 60:
    print("eligible")
else:
    print("not eligible")

ssc = 60
hsc = 50

if ssc >= 70 or hsc >= 60:
    print("eligible")
else:
    print("not eligible")


# NOT operators

ssc = 70
hsc = 80
criminal = True

if ssc >= 60 or hsc >= 60 and criminal:
    print("not eligible")
else:
    print("eligible")


ssc = 70
hsc = 80
criminal = True

if ssc >= 60 or hsc >= 60 and not criminal:
    print(" eligible")
else:
    print("not eligible")
