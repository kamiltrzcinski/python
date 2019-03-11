import random
import math


def makeV(tab):
    i = 0
    while i < 10:
        tab.append(random.randrange(0, 20, 1))
        i += 1
    return tab

def lngV(tab):
    lng = 0
    for x in tab:
        lng+=x*x
    lng=math.sqrt(lng)
    return lng



vector1 = []
vector2 = []

makeV(vector1)
makeV(vector2)

sclV = 0

i=0
while i<10:
    sclV+=vector1[i]*vector2[i]
    i+=1

print(sclV)
lngV1 = (lngV(vector1))
lngV2 = (lngV(vector2))

cosV = sclV/(lngV1*lngV2)
cosV = math.acos(cosV)
cosV = round(math.degrees(cosV))
print(cosV)
