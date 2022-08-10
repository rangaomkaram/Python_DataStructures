# Largest 3-same-Digit Number in sring
"""
# you are given a string num represting a large integer. An
Integer is good if it meets the follwing conditions:
1. It  is a substring of num with length 3.
2. It consists of only one unique digit 

Return the maximum good integer as a string or an emoty string"
if no such integer exists

Note :

1. A substring is a contigous sequence of characters within a string.
2. There may be leading zeros in num or good integer.
"""

class Solution:
    def largestGoodInteger(self,num:str)->str:
        N=len(num)
        best = " "
        for i in range(N):
            if i +2 < N and num[i] == num[i +1] and num[i] == num[i+2]:
                best = max(best,num[i:i+3])
        return best        

