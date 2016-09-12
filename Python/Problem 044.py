from time import clock


def pentagon(n):  # Pn=n(3n−1)/2
    return n * (3 * n - 1) / 2


def main():
    start = clock()

    pent_nums = [pentagon(n) for n in range(1, 10001)]

    D = pent_nums[-1]
    print(D)
    pair = [0, 0]

    for (j, p1) in enumerate(pent_nums):
        print(p1)
        for (k, p2) in enumerate(pent_nums[j + 1:]):
            isPentagon = (p1 + p2) in pent_nums and (p2 - p1) in pent_nums
            if p2 - p1 < D and isPentagon:
                D = p2 - p1
                pair = [p1, p2]
                break
        if pair != [0, 0]:
            break
    print(pair, D)
    print(clock() - start)


if __name__ == '__main__':
    main()
