""" Given an array height that contains height of each bar in the histogram, we are asked to 
return the area of the largest rectangle in the histogram.Note that eachbar has a width of 1
|heights| >=1 heights[i] >=0

"""

def largest_rectangle(h):
    max_area = 0
    for i in range(len(h)):
        left = i
        while left -1 >=0 and h[left-1] >= h[i]:
            left -= 1
        right = i
        while right+1 < len(h) and h[right+1] >= h[i]:
            right += 1
        max_area = max(max_area,h[i]*(right-left+1))
    return print(max_area)

h= [3,2,4,5,7,6,1,3,8,9,10,11,10,7,5,2,6]

largest_rectangle(h=h)