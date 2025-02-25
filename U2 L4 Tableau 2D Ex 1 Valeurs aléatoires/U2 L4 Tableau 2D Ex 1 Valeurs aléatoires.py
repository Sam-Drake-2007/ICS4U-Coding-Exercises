# ICS4U U2 L4 Tableau 2D Ex 1 Valeurs aléatoires

import numpy as np
import random

col = []

arr = np.random.randint(100, size=(6,6))
print(arr)
print("")

count = 0
for row in arr:
    print(f"La somme de la rangée {count} est {sum(row)}")
    count += 1

print("")
for i in range(len(arr)):
    for row in arr:
        col.append(row[i])
    print(f"La somme de la colone {i} est {sum(col)}")
    col = []
