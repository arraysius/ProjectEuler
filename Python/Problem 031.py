from time import clock

start = clock()

amount = 1000
combinations = 0
for a in range(2):
    for p100 in range(3):
        for p50 in range(5):
            for p20 in range(11):
                for p10 in range(21):
                    for p5 in range(41):
                        for p2 in range(101):
                            for p1 in range(201):
                                total = (a * 200 + p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2 + p1)
                                if total == amount:
                                    combinations += 1
                                elif total > amount:
                                    break
                            if (a * 200 + p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2) > amount:
                                break
                        if (a * 200 + p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5) > amount:
                            break
                    if (a * 200 + p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10) > amount:
                        break
                if (a * 200 + p100 * 100 + p50 * 50 + p20 * 20) > amount:
                    break
            if (a * 200 + p100 * 100 + p50 * 50) > amount:
                break
        if (a * 200 + p100 * 100) > amount:
            break

print(combinations)
print(clock() - start)
