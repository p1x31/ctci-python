for a1, b in t1:
    for a2, c in t2:
        if a1 == a2:
            t3.append((a1, b, c))
for row in t1:
    t1_map[row[0]] = row

def left():
    for a, b in t1_map.items():
        if a in t2_map:
            t3.append((a, b, t2[a]))
        else:
            t3.append((a, b, 'NULL'))

def full():
    for a, c in t2_map.items():
    if a not in t1_map:
        t3.append((a, 'NULL', c))