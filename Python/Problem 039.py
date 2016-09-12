from time import clock
import math


def py_tri_v3(limit):
    total = 0
    for a in range(1, limit):
        for b in range(a + 1, limit):
            if a + b >= p:
                break
            c = math.ceil(math.sqrt(a ** 2 + b ** 2))
            if a + b + c == p and a ** 2 + b ** 2 == c ** 2:
                total += 1
    return total


start = clock()

solutions = 0
number = 0
for p in range(1001, 6, -1):
    sols = py_tri_v3(p)
    if sols > solutions:
        solutions = sols
        number = p

print(number, solutions)
print(clock() - start)
