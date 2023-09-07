s = input()
sheriff = 'sheriff'
count = 0
while len(s) >= len(sheriff):
    for i in sheriff:
        if i in s:
            s = s[s.index(i)+1:]
        else:
            break
    else:
        count += 1
print(count)