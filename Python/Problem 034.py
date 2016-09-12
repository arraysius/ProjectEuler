from time import clock
from math import factorial

start = clock()

total = 0
nums = []
for n in range(3, 1000000):
    num_string = str(n)
    fac_sum = 0
    for s in num_string:
        fac_sum += factorial(int(s))
    if fac_sum == n:
        total += n
        nums.append(n)

print(total, nums)
print(clock() - start)
