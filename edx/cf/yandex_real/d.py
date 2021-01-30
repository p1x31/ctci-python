from sys import stdin,stdout
from collections import Counter
freq = {}
for num in map(str, input().strip().split()):
    freq[num] = freq.get(num, 0)+1
print(len(freq.values()))