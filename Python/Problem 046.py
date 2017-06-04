import time

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

def issqrt(num):
    return num ** 0.5 == int(num ** 0.5)

def confirm_conjecture(num, primes):
    for p in primes:
        if p >= num:
            break
        elif issqrt((num - p) / 2):
            return True
    return False

def main():
    start = time.time()

    UPPER_LIMIT = 10000
    primes = prime_sieve(UPPER_LIMIT)
    odd_composites = [x for x in range(9, UPPER_LIMIT) if x not in primes and x % 2 != 0]

    for n in odd_composites:
        if not confirm_conjecture(n, primes):
            print(n)
            break

    print('\n{}s'.format(time.time() - start))

if __name__ == '__main__':
    main()
