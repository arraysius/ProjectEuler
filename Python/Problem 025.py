from time import clock

start = clock()

digits = 1000

a = 1
b = 1
temp = 0
i = 2

while True:
    temp = a + b
    a = b
    b = temp
    i += 1
    if len(str(b)) == digits:
        print(i)
        break

print(clock() - start)