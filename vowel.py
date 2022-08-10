name = str(input("Enter the characters or string:"))
count = 0
for ch in name:
    if ch in 'aeiouAEIOU':
        count += 1
print("Total vowels in sentence in",name,'is:',count)