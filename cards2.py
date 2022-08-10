from turtle import position



def locate_cards(cards,query):
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return print(position)
        position += 1
    return print(-1)

cards = []
query = 7

locate_cards(cards=cards,query=query)