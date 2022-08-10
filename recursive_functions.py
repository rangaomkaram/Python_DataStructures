# recursive function that prints lenght of the string

def reclen(char1):
    if char1 == '':
        return 0
    else:
        return 1 + reclen(char1[1:])

string1 = "Rangaseshaudaykumarraju"

print(reclen(char1=string1))

count = 0
for i in string1:
    count += 1
print(count)
    


