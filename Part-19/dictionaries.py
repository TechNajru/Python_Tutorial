# dictionaries are the one which stores information in key and value pairs

dic1 = {"x": 20, "y": 40}
print(dic1)

dic2 = dict(name="najru", roll=20)
print(dic2)

dic1["x"] = 100
print(dic1)

dic1["z"] = 45
print(dic1)

if "name" in dic2:
    print(dic2["name"])

del dic1["x"]
print(dic1)

del dic1["z"]
print(dic1)
