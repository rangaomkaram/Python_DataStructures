def rec(heights,low,high):
    if low > high:
        return 0
    elif low == high:
        return heights[low]
    else:
        minh       = min(heights[low:high+1])
        pos_min    = heights.index(minh,low,high+1)
        from_left  = rec(heights,low,pos_min-1)
        from_right = rec(heights,pos_min+1,high)
        #result     = max(from_left,from_right,minh*(high-low+1))
        return print(from_right)

def largest_rectangle(heights):
    return rec(heights,0,len(heights)-1)

heights = [3,2,4,5,7,6,1,3,8,9,10,11,10,7,5,2,6]

largest_rectangle(heights=heights)