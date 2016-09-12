from time import clock


def dec_bin_palindrome_check(number):
    dec_s = str(number)
    bin_s = str(bin(number))[2:]
    return dec_s == dec_s[::-1] and bin_s == bin_s[::-1]


start = clock()

palindromes = []

for n in range(1000000):
    if dec_bin_palindrome_check(n):
        palindromes.append(n)

print(sum(palindromes), palindromes)
print(clock() - start)
