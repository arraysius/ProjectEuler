from fractions import Fraction
from time import clock

start = clock()


def repeated_digit(i, j):
	for k in str(i):
		for l in str(j):
			if k == l:
				return k
	return False


final_fraction = 1

for i in range(10, 100):
	for j in range(i + 1, 100):
		if i % 10 == 0 and j % 10 == 0:
			continue

		digit = repeated_digit(i, j)
		if digit:
			i_s = int(str(i).replace(digit, '', 1))
			j_s = int(str(j).replace(digit, '', 1))
			if j_s != 0 and (i_s / j_s) == (i / j):
				final_fraction *= Fraction(i, j)

print(final_fraction)
print(clock() - start)
