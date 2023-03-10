t = int(input())
for i in range(t):
    m = int(input())
    s = input()
    bills = {}
    pay = {}
    data_list = s.split(",")
    for data in data_list:
        pair = data.split(":")
        bills[int(pair[0])] = int(pair[1])
    bills = dict(sorted(bills.items(), reverse=True))
    for bill in bills.keys():
        while m >= bill and bills[bill] > 0:
            if pay.get(bill) == None:
                pay[bill] = 1
            else:
                pay[bill] += 1
            m -= bill
            bills[bill] -= 1
    print(f'Customer{i + 1}:')
    if m == 0:
        for key in pay.keys():
            print(f'{key} {pay[key]}')
    else:
        print('Impossible')