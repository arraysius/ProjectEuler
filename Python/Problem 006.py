sum_of_sqaures = 0
square_of_sums = 0

for x in range(1, 101):
    sum_of_sqaures += x ** 2
    square_of_sums += x

print((square_of_sums ** 2) - sum_of_sqaures)
