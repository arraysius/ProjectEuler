weekday = 1
count = 0

for year in range(1901, 2001):
    isLeap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        isLeap = True

    for month in range(1, 13):
        days = 0
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days = 31
        else:
            if month == 2:
                if isLeap:
                    days = 29
                else:
                    days = 28
            else:
                days = 30

        if weekday == 6:
            count += 1

        weekday = (weekday + days) % 7

print(count)
