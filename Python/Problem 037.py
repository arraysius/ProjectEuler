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


def truncate_left(num):
    num_s = str(num)
    for x in range(len(num_s)):
        if int(num_s[x:]) not in prime_set:
            return False
    return True


def truncate_right(num):
    num_s = str(num)
    for x in range(len(num_s), 0, -1):
        if int(num_s[:x]) not in prime_set:
            return False
    return True


start = clock()

truncatable_primes = []
prime_set = set(prime_sieve(1000000))

for p in prime_set:
    if p > 7 and truncate_left(p) and truncate_right(p):
        truncatable_primes.append(p)

print(sum(truncatable_primes), truncatable_primes)
print(clock() - start)
