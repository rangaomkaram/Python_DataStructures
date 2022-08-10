# list Comprehension
# for the short cuts for the loop iterables 

"""
1.List Comprehension

syntax :
        list_variable = [expression for values in iterable if condition]

"""
numberlist = [9,56,7,8454,745,246,7563,73524456,6553623,6632,5345]
evenlist = [i for i in numberlist if i%2==0]
print("Evenlist are:",evenlist)

oddlist = [i for i in numberlist if i%2!=0]
print("Oddlist are:", oddlist)

squarelist = [i**2 for i in numberlist]
print("Square List are :" , squarelist)

"""
Set Comprehension :

syntax:

set_variables = {expression for values in iterable if condition}

"""
square_set = {i**2 for i in numberlist}

print(square_set)

sqdict = {i:i**2 for i in numberlist}

print("sqdict:", sqdict)





