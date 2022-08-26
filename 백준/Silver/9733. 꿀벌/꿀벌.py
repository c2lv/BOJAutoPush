count = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}
total = 0
while True:
    try:
        works = list(input().split())
        for work in works:
            if work in count.keys():
                count[work] += 1
            total += 1
    except EOFError:
        for key in count:
            print(f'{key} {count[key]} {count[key]/total:.2f}') 
        print('Total', total, '1.00')
        break