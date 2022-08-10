"""
Given a sorted array of integers arr and an integer ourourtarget,
find the index of the first and last position of ourtarget in arr.
In ourtarget can't be found in arr , return [-1,-1]
"""

# output = [2,6]

def first_and_last1(arr,ourtarget):
    for i in range(len(arr)):
        if arr[i] == ourtarget:
            start = i
            while i+1 <len(arr) and arr[i +1] == ourtarget:
                i = i +1 
            return print([start,i])
    return print([-1,-1])
# given array must be sorted 
arr = [2,4,5,5,5,5,5,7,9,9,10,10,10,10,10]
ourtarget = 10
first_and_last1(arr=arr,ourtarget=10)

"""Using binary Search"""

"""
Approach one is the binary search only for left or start position to find used
"""

def first_start(arr,ourtarget):
    if arr[0] == ourtarget:
        return 0
    left ,right = 0,len(arr)-1
    while left <=right:
        mid = (left+right)//2
        if arr[mid] == ourtarget and arr[mid-1] < ourtarget :
            return mid
        elif arr[mid] < ourtarget:
            left = mid + 1 
        else:
            right = mid -1
    return -1

def first_and_last2(arr,ourtarget):
    if len(arr) == 0:
        return print([-1,-1])
    start = first_start(arr,ourtarget)
    if start == -1:
        return print([-1,-1])
    end = start
    while end +1 < len(arr) and arr[end +1] == ourtarget:
        end += 1
    return print([start,end])
arr = [2,4,5,5,5,5,5,7,9,9,10,10,10,10,10]
ourtarget = 10
first_start(arr=arr,ourtarget=ourtarget)
first_and_last2(arr=arr,ourtarget=ourtarget)


"""
using binary search for finding the last position 
"""

