from time import clock


def main():
    start = clock()

    total = 0

    for n in range(1, 1001):
        total += n ** n

    print(str(total)[-10:])

    print(clock() - start)


if __name__ == '__main__':
    main()
