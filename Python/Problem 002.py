num1 = 1
num2 = 2
temp = 0
sum = 0

while num2 < 4000000:
    if num2 % 2 == 0:
       sum += num2
    temp = num1 + num2
    num1 = num2
    num2 = temp

print(sum)