"""
Question 1:
ALice has some cards with numbers written on them.She arranges
the cards in decreasing order, and lays on them out face down
in a sequence on a table.She challanges Bob to pick up
card containing a given number by turning over as few cards
as possible.

"""
"""
The Method you may get some ideas on how to slove it
and 

"""
from turtle import position


cards = [13,11,10,7,4,3,1,0]
query = 1
output = 3

def locate_cards(cards,query):
    position = 0

    while True:
        if cards[position] == query:
            return print(position)
        
        position +=1
        
        if position == len(cards):

            return print(-1)
        
locate_cards(cards=cards,query=query)













