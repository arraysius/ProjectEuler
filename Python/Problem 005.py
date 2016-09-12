current_num = 1

while True:
    divisible = True
    for x in range(20, 1, -1):
        if current_num % x != 0:
            divisible = False
            current_num += 1
            break

    if divisible:
        print(current_num)
        break