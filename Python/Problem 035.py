from time import clock
from itertools import permutations


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


def rotate(number):
    charset = str(number)
    rots = []

    rot = str(number)
    for i in range(len(charset)):
        rot = rot[1:] + rot[0]
        rots.append(int(rot))

    return rots


start = clock()

prime_nums = prime_sieve(1000000)
circular_primes = []

for n in prime_nums:
    rotations = rotate(n)
    all_prime = True
    for r in rotations:
        if r not in prime_nums:
            all_prime = False
            break
    if all_prime:
        circular_primes.append(n)

print(len(circular_primes), circular_primes)
print(clock() - start)
