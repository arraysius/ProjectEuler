import time

start_time = time.time()

largest_chain = 0
start_num = 0

for num in range(1, 1000000):
    num_temp = num
    chains = 1
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = (3 * num) + 1
        chains += 1
    if chains > largest_chain:
        largest_chain = chains
        start_num = num_temp
print(start_num, largest_chain)
print(time.time() - start_time)