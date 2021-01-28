s = str(input())
bal = 0
def correct(s):
    
    for i in range(len(s)):
        if s[i] == "(":
            bal += 1
        else:
            bal -= 1
        if (bal < 0):
            return False
    return (bal == 0)

def rec(idx, bal):
    if (idx == 2*n):
        if bal == 0:
            print(s)
        return
    s[idx] = "("
    rec(idx+1, bal+1)
    if bal == 0:
        return
    s[idx] = ")"
    rec(idx + 1, bal - 1)

rec(0,0)