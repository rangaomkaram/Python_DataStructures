from collections import defaultdict
from ntpath import join

def group_anagram(a):
    dfdict =defaultdict(list)
    for i in a:
        sorted_i = "".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()



words = ['state','tea','taste','cat','eat','act','crate']
print(group_anagram(words))