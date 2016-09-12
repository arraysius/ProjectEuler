import time
import math


def d(n):
    total = 1
    root = math.sqrt(n)
    for x in range(2, int(root) + 1):
        if n % x == 0:
            total += x + (n / x)
    if root == int(root):
        total -= root
    return total


if __name__ == '__main__':
    start = time.clock()

    limit = 28123
    s = 0
    abundant = set()

    for num in range(1, limit + 1):
        if d(num) > num:
            abundant.add(num)
        abundant_sum = False
        for abn in abundant:
            if (num - abn) in abundant:
                abundant_sum = True
                break
        if not abundant_sum:
            s += num

    print(s)
    print(time.clock() - start)
