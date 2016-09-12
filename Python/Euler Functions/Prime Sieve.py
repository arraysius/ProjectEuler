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


start = clock()
print(prime_sieve(1000))
print(clock() - start)
