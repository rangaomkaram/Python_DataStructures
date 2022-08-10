#recersive

def msg(n):
    print("Hello Ranga",n)
    if n > 1:
        msg(n-1)
msg(6)

def fact(n):
    if n == 1:
        return 1
    else:
        return (n*fact(n-1))
    
print(fact(7))