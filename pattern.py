n = int(input("Enter the number of rows:"))

for row in range(n):
    for space in range(row+1):
        print(' ',end='')
    for col in range(row,n-1):
        print('*',end='')
    for col2 in range(row,n):
        print('*',end='')
    print()

for row in range(1,4):
    for col in range(1,4):
        if(row+col)%2==1:
            print('*',end='')
        else:
            print(' ',end='')
    print()