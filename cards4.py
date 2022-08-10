def test_location(cards,query,mid):
    mid_number = cards[mid]
    print("mid:",mid,",mid_number:",mid_number)

    if mid_number == query:
        if mid-1 >=0 and cards[mid-1] == query:
            return print("left")
        else:
            return print("found")
        elif mid_number < query:
            return print("left")
        else:
            return print("right")

def locate_cards(cards,query):
    lo, hi = 0 ,len(cards) -1

    while lo <= hi:
        print("lo:",lo,",hi:",hi)
        mid = (lo + hi) // 2
        result = test_location(cards,query,mid)

        if result == "found":
            return print("mid")
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return print(-1)