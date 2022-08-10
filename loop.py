n = int(input("Enter the number of rows:"))

for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=" ")
    print()

for row in range(1,n+1):
    for col in range(row,n):
        print('*',end=" ")
    print()

for row in range(n):
    for space in range(row,n):
        print(" ",end="")
    for col in range(row+1):
        print('*',end='')
    print()
