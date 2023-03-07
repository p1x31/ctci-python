#creating evens

evens = [x for x in range(10) if x % 2 == 0]

evens = [x for x in 0..10 if x % 2 == 0]

evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)

evens = {x for x in range(10) if x % 2 == 0}