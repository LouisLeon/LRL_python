from collections import defaultdict

d = defaultdict(list)


mylist = [(1, 2), (1, 4), (5, 6)]

for k, v in mylist:
    d[k].append(v)

r = dict(d)
print(r)


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1},
             'Alice': {'apples': 5, 'pretzels': 12}}


def totalBrought(guests, item):
    total = 0
    for k, v in guests.items():
        total += v.get(item, 0)
    return total


print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
