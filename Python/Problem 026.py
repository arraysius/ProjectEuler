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

longest_sequence = 0
for d in prime_sieve(1000)[::-1]:
    if longest_sequence >= d:
        break
    remainders = []
    value = 1
    while value not in remainders:
        value %= d
        remainders.append(value)
        value *= 10
    if (len(remainders) - remainders.index(value / 10)) > longest_sequence:
        longest_sequence = (len(remainders) - remainders.index(value / 10))

print(longest_sequence)
print(clock() - start)
