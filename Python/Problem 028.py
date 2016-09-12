from time import clock

start = clock()

length = 1001
num = length * length
total = num

for x in range(length - 1, 1, -2):
    for y in range(4):
        num -= x
        total += num

print(total)

print(clock() - start)
