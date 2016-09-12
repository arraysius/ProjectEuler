from itertools import permutations
import time

start = time.clock()

perms = [''.join(p) for p in permutations('0123456789')]

print(perms[999999])
print(time.clock() - start)