import time

import math

start = time.time()

n_factors = 500
n = 1
while True:
    f = 0
    triangle = int((n * (n + 1)) / 2)

    for x in range(1, int(math.floor(math.sqrt(triangle))) + 1):
        if triangle % x == 0:
            f += 2

    if f >= n_factors:
        print(triangle, f)
        break
    n += 1

print(time.time() - start)