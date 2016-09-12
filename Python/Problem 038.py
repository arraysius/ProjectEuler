from time import clock

start = clock()

largest = 0
number = 0

for n in range(1000000):
    pandigital = ''
    for x in range(1, 10):
        if len(pandigital) < 9:
            pandigital += str(n * x)
        elif ''.join(sorted(pandigital)) == '123456789':
            if int(pandigital) > largest:
                largest = int(pandigital)
                number = n
            break
        else:
            break

print(largest, number)
print(clock() - start)