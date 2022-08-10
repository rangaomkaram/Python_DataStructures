def kth_permutation(n,k):
    permutation = []
    unused = list(range(1,n+1))
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1]
    k -=1  
    while n > 0:
        part_length = fact[n]//n
        i = k//part_length
        permutation.append(unused[i])
        unused.pop(i)
        n -= 1
        k %=  part_length
    return print(''.join(map(str,permutation)))

kth_permutation(n=5,k=20)


""" def contains_all(freq1,freq2):
    for ch in freq2:
        if freq1[ch] < freq2[ch]:
            return True """

