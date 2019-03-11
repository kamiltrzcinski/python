import random
import math


def max(tab):
    m = tab[0]
    for i in tab:
        if i > m:
            m = i
    return m

def min(tab):
    m = tab[0]
    for i in tab:
        if i < m:
            m = i
    return m


table = []

i = 0
while i < 30:
    table.append(random.randrange(0, 100, 1))
    i+=1

xMin = min(table)
xMax = max(table)
print(xMin)
print(xMax)
print()

table.sort()
for x in table:
    print (x)

mid = 0
stdDiv = 0


for x in table:
    mid+=x
mid/=30

for x in table:
    stdDiv+=(i-mid)*(i-mid)
stdDiv/=30
stdDiv=math.sqrt(stdDiv)

print()
print(mid)
print(stdDiv)
print()

for x in table:
    x=(x-xMin)/(xMax-xMin)
    print(x)

for x in table:
    x=(x-mid)/stdDiv
    print(x)