biggest_palindrome_num = 0

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        num = x * y
        if str(num) == str(num)[::-1] and num > biggest_palindrome_num:
            biggest_palindrome_num = num

print(biggest_palindrome_num)