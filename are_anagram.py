"""
Using Hash Table -> Implemenataion of the set or map 
where set remove duplicates and decome data with less redundancy
Dictionaries or hashtable

"""
"""Driver Code"""
s1 = "nameless"
s2 = "salesmen"

def Anagram(s1,s2):
    if len(s1) != len(s2):
        return print('length of anagrams are not equal')
    freq1 = {}
    freq2 = {}
    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return print('They are not anagram')
    return print('the both strings are anagram')


Anagram(s1,s2)
