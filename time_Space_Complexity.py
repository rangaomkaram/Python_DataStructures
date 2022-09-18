"""
Big O notation is used to measure the time and space complexity requirements for your program 
grows as inputsize grows.

time = a * n + b -> Keep fastest growing term -> time = a * n ->Drop Constants -> time = O(n)


"""


import numbers


def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return print(squared_numbers)

numbers = [2,5,8,9]
get_squared_numbers(numbers)