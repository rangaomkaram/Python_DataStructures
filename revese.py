# get the string reverse order

name = str(input("Enter the Name:"))

rev=""

for index in range(len(name)-1,-1,-1):
    rev = rev + name[index]
print('Name:',name)
print('Reverse Name:',rev)