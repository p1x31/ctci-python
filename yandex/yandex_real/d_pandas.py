import pandas as pd
n = int(input())
a = [] 
for _ in range(n):
    a.append(str(input()))
print(pd.Series(a).nunique())