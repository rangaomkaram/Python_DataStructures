""" def descending_order(num):
    return print(int(str(num)[::-1]))


descending_order(num= 1452634) """


""" def descending_order(num):
    return print(int(''.join(sorted(str(num), reverse=True)))) """

def descending_order(num):
    return print(int(num)[::]-1)


descending_order(num= 1452634)
