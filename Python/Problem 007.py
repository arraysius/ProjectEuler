import time

def nth_prime(n):
    primes = [2]
    num = primes[-1]
    while True:
        if len(primes) == n:
            break

        if num % 2 == 0:
            num += 1
        else:
            num += 2

        isPrime = True
        for x in primes:
            if num % x == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(num)

start = time.time()
nth_prime(10001)
print(time.time() - start)
