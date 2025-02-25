
import numpy as np
from scipy import stats

arr = []

count = 1
while True:
    val = input(f"Entrer valeur {count} (Q/q pour quitté): ")
    try:
        val = int(val)
    except:
        break
    arr.append(val)
    count += 1

arr = np.array(arr)
mode = stats.mode(arr)

print(f"\nLa liste est: {arr}")
print(f"\nLa moyenne est: {np.mean(arr)}")
print(f"La médianne est: {np.median(arr)}")
print(f"Le mode est: {mode}")