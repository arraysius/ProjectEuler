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


def digit_freq(num):
	freq = dict()
	for d in num:
		if d in freq:
			freq[d] += 1
		else:
			freq[d] = 1
	return freq


def main():
	start = clock()

	largest_pandigital_prime = 0

	for prime in prime_sieve(100000000):
		a = digit_freq(str(prime))
		b = digit_freq(''.join([str(d) for d in range(1, len(str(prime)) + 1)]))
		if a == b:
			largest_pandigital_prime = prime

	print(largest_pandigital_prime)
	print(clock() - start)


if __name__ == '__main__':
	main()
