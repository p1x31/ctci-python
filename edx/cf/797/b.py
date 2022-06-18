import copy
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #print(a)
    #print(b)
    mutableA = copy.deepcopy(a) 
    
    if any([a[i] < b[i] for i in range(n)]):
         print("NO")
    else:
        mx = max(a) - max(b)
        for j in range(mx + 2): 
            sub_a = ([element - j for element in mutableA if element >= 0]) 
            sub_a = [0 if z <= 0 else z for z in sub_a]
            #sub_a = [(z >= 0) * z for z in sub_a] 
            print(sub_a) 
            if sub_a == b: 
                print("YES") 
                break 
            #elif max(sub_a) == 1 and (sub_a[0] != 1): 
            elif sum(sub_a) == 0:
                print("NO") 
            else:
                continue
            
