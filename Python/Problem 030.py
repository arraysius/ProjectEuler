from time import clock

start = clock()

nums = []
for n in range(2, 1000000):
    num_string = str(n)
    sum = 0
    for s in num_string:
        sum += int(s) ** 5
    if sum == n:
        nums.append(n)

total = 0
for x in nums:
    total += x

print(total, nums)
print(clock() - start)