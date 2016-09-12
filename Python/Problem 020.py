import math

num = str(math.factorial(100))
total = 0
for x in num:
    total += int(x)
print(total)