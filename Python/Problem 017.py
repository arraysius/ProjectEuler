ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens_1x = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
           17: 'seventeen',
           18: 'eighteen', 19: 'nineteen'}
tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

letters = 0

for x in range(1, 10):
    letters += len(ones[x])                     # 1 - 9

for x in range(10, 20):
    letters += len(tens_1x[x])                  # 10 - 19

for x in range(20, 100):
    letters += len(tens[int(str(x)[0])])        # tens
    if str(x)[1] != '0':
        letters += len(ones[int(str(x)[1])])    # ones

for x in range(100, 1000):
    letters += len(ones[int(str(x)[0])]) + 7    # hundreds + 'hundred'
    if str(x)[1] != '0' or str(x)[2] != '0':
        letters += 3                            # 'and'
        if str(x)[1] == '1':
            letters += len(tens_1x[int(str(x)[1:3])])    # 10 - 19
        else:
            if str(x)[2] != '0':
                letters += len(ones[int(str(x)[2])])    # ones
            if 1 < int(str(x)[1]) <= 9:
                letters += len(tens[int(str(x)[1])])    # tens

letters += len('onethousand')

print(letters)
