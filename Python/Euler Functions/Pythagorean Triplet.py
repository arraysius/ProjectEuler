from time import clock

import math


def py_tri_v1(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                if a ** 2 + b ** 2 == c ** 2:
                    triplets.append([a, b, c])

    return triplets


def py_tri_v2(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a + 1, limit):
            for c in range(b + 1, limit):
                if a ** 2 + b ** 2 == c ** 2:
                    triplets.append([a, b, c])
    return triplets


def py_tri_v3(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a + 1, limit):
            c = math.ceil(math.sqrt(a ** 2 + b ** 2))
            if a ** 2 + b ** 2 == c ** 2:
                triplets.append([a, b, c])
    return triplets


start = clock()
print(py_tri_v3(100))
print(clock() - start)
