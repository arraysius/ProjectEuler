from time import clock


# Triangle      Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
# Pentagonal    Pn=n(3n−1)/2    1, 5, 12, 22, 35, ...
# Hexagonal     Hn=n(2n−1)      1, 6, 15, 28, 45, ...

def triangle(n):
    return n * (n + 1) / 2


def pentagon(n):
    return n * (3 * n - 1) / 2


def hexagon(n):
    return n * (2 * n - 1)


def main():
    start = clock()

    begin = 285
    limit = 100000 + 1
    tri = [triangle(n) for n in range(begin, limit)]
    pent = set(pentagon(n) for n in range(begin, limit))
    hex = set(hexagon(n) for n in range(begin, limit))

    for t in tri:
        if t in pent and t in hex:
            print(t)
            break

    print(clock() - start)


if __name__ == '__main__':
    main()
