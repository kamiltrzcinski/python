import random
import matplotlib.pyplot as plt


def makeV(tab):
    i = 0
    while i < 100:
        tab.append(random.randrange(0, 21, 1))
        i += 1
    return tab


vector = []
makeV(vector)

tab = dict([(x, vector.count(x)) for x in vector])
print(tab)
plt.bar(*zip(*tab.items()))
plt.show()
