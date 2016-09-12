import math
from time import time

start = time()

for a in range(1, 1001):
    for b in range(a + 1, 1001):
        if (float(a + b) + math.sqrt(a ** 2 + b ** 2)) == float(1000):
            c = math.sqrt(a ** 2 + b ** 2)
            print(a, b, c, a * b * c)

print('\n', time() - start)