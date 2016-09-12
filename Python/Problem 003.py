def nextPrime(current_prime):
    while True:
        current_prime += 1
        isPrime = True
        for y in range(current_prime - 1, 1, -1):
            if current_prime % y == 0:
                isPrime = False
                break

        if isPrime:
            return current_prime


if __name__ == '__main__':
    num = 600851475143

    current_prime = 2
    primes_of_num = []

    while num > 1:
        if num % current_prime == 0:
            primes_of_num.append(current_prime)
            while num % current_prime == 0:
                num /= current_prime
        current_prime = nextPrime(current_prime)

    print(primes_of_num)
