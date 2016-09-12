from time import clock


def prime_sieve(limit):
    numbers = [True] * limit
    numbers[0] = numbers[1] = False
    primes = set()

    for (i, isPrime) in enumerate(numbers):
        if isPrime:
            primes.add(i)
            for x in range(i * i, limit, i):
                numbers[x] = False
    return primes


def main():
    start = clock()

    primes = prime_sieve(1000000)

    max_primes = 0
    product = 0

    for a in range(-999, 1000):
        for b in range(-999, 1000):
            for n in range(100):
                if (n ** 2) + (a * n) + b not in primes:
                    break
                if n + 1 > max_primes:
                    max_primes = n + 1
                    product = a * b

    print(product, max_primes)
    print(clock() - start)


if __name__ == '__main__':
    main()
