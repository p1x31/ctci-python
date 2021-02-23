s = str(input())
# if len(s) % 2 == 0:
#     for i in (0,len(s),2):
#         if s[i].islower() and s[i+1].isupper():
#             continue
#         else:
#             print("No")
#             break
l = str()
u = str()

for i in range(0, len(s)):
    if (i % 2 == 0) or i == 0:
        l = l + s[i] 
    else:
        u = u + (s[i])
if any(filter(str.islower, u)) or any(filter(str.isupper, l)):
    print("No")
else:
    print("Yes")