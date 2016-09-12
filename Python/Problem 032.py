from time import clock

start = clock()

total = 0
pandigital = []
limit = 2000
for x in range(1, limit):
    if '0' in str(x):
        continue
    for y in range(x + 1, limit):
        if '0' in str(y):
            continue
        product = x * y
        s_num = str(x) + str(y) + str(product)
        if len(s_num) > 9:
            break
        if ''.join(sorted(s_num)) == '123456789' and product not in pandigital:
            total += product
            pandigital.append(product)

print(total, pandigital)
print(clock() - start)
