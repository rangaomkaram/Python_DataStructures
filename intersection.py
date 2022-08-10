x = [1,5,0,9]
y = [3,0,2,9]

## return [9,0]
# 
def intersection(x,y):
    result = [value for value in x if value in y]
    return sorted(result,reverse=True)

print(intersection(x,y)) 
