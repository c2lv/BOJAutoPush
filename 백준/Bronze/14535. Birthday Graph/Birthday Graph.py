MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
x = 1
while True:
    n = int(input())
    if n == 0:
        break
    birth = [0 for _ in range(12)]
    for i in range(n):
        month = input()
        month = int(month[3:5]) - 1
        birth[month] += 1
    print(f"Case #{x}:")
    for i in range(12):
        print(f"{MONTHS[i]}:{'*' * birth[i]}")
    x += 1