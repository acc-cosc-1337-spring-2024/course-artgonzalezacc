#main program
import lists

names = []
option = "Y"

while option.upper() == 'Y':

    item = input("Enter name: ")

    names.append(item)
    option = input("Enter y to continue ")

for name in names:
    print(name)

item = input("Enter name: ")
index = names.index(item)

names[index] = "Modified"

for name in names:
    print(name)