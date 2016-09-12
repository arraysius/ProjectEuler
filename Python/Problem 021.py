import time

import math

start = time.time()


def d(n):
    total = 1
    for x in range(2, math.ceil(math.sqrt(n))):
        if n % x == 0:
            total += x
            if (n / x) != x:
                total += (n / x)
    return total


amicable_nums = set()

for a in range(1, 10000):
    if a not in amicable_nums:
        b = d(a)
        if d(a) == b and d(b) == a and a != b:
            amicable_nums.add(a)
            amicable_nums.add(b)

sum = 0
for x in amicable_nums:
    sum += x
print(sum)
print(amicable_nums)

print(time.time() - start)
