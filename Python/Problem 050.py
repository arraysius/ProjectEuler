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


def main():
    start = clock()

    limit = 1000000
    primes = prime_sieve(limit)

    largest = 0
    terms = 0

    for i in range(0, len(primes)):
        total = 0
        adds = 0
        for j in range(i, len(primes)):
            total += primes[j]
            adds += 1
            if total >= limit:
                break
            elif total in primes and adds > terms:
                largest = total
                terms = adds

        if total >= limit:
            break

    print(largest, terms)

    print(clock() - start)


if __name__ == '__main__':
    main()
