# file Operations on a file in python
# It include opening,reading,writing ,closing a file

from pathlib import Path
import os
file = open("Part-23\\example.txt", "r")      # open a file in read mode

file = open("Part-23\\example.txt", "r")
file_content = file.read()           # Reads entire file
print(file_content)

print("")

file = open("Part-23\\example.txt", "r")
line = file.readline()         # Reads one line
print(line)

print("")

file = open("Part-23\\example.txt", "r")
lines = file.readlines()       # Reads all lines into a list
print(lines)
file.close()


file = open("Part-23\\example.txt", "w")
file.write("Hello, World! \n")  # Write sentence in first line of .txt file
# Write 2nd and 3rd line in .txt file
file.writelines(["I am  2\n", "Najrudeen 3\n"])
file.close()

# No need to manually close, it's done automatically!
with open("Part-23\\example.txt", "r") as file:
    content = file.read()
print(content)


path = Path("Part-23\\example.txt")
if path.exists():
    print("File exists!")
else:
    print("file don't exist")
