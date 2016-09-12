from time import clock


def prime_sieve(limit):
    numbers = [True] * limit
    numbers[0] = numbers[1] = False
    primes = []

    for (i, isPrime) in enumerate(numbers):
        if isPrime:
            primes.append(i)
            for x in range(i * i, limit, i):
                numbers[x] = False
    return primes


def isPandigital(n):
    strn = sorted(str(n))



def main():
    start = clock()

    primes = prime_sieve(1000000)

    print(clock() - start)


if __name__ == '__main__':
    main()
