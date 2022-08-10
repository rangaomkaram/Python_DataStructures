def binary_search(lo,hi,condition):
    while lo <= hi:
        mid = (lo + hi) //2
        result = condition(mid)
        if result == "found":
            return print(mid)
        elif result == "left":
            hi = mid - 1
        
        else:
            lo = mid + 1
    
    return print(-1)


def locate_card(cards,query):

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return print('left')
            else:
                return print("found")
        elif cards[mid] < query:
            return print('left')
        else:
            return print('right')
    
    return binary_search(0,len(cards) - 1, condition)