from itertools import permutations
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

    perms = [''.join(p) for p in permutations('0123456789')]
    primes = prime_sieve(18)
    print(primes)

    total = 0

    for p in perms:
        divPrime = True
        for x in range(1, 8):
            if divPrime == False:
                break
            num = int(p[x:x + 3])
            if num % primes[x - 1] == 0:
                divPrime = divPrime and True
            else:
                divPrime = divPrime and False
        if divPrime == True:
            total += int(p)

    print(total)
    print(clock() - start)


if __name__ == '__main__':
    main()
