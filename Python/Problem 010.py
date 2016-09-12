import time


def prime_sieve(limit):
    numbers = [True] * limit
    numbers[0] = numbers[1] = False
    sum = 0

    for (i, isPrime) in enumerate(numbers):
        if isPrime:
            sum += i
            for x in range(i*i, limit, i):
                numbers[x] = False
    return sum

start = time.time()
sum = prime_sieve(2000000)
elapsed = time.time() - start
print(sum, elapsed)
