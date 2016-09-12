from time import clock


def main():
    start = clock()
    
    terms = set()

    for a in range(2, 101):
        for b in range(2, 101):
            terms.add(a**b)

    print(len(terms))
    
    print(clock() - start)

if __name__ == '__main__':
    main()
