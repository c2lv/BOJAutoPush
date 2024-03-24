import sys
input = lambda: sys.stdin.readline().rstrip()

def display_sorted_list(data):
    sorted_data = sorted(data, key=lambda x: (-x[2]*x[1], -x[1], x[0]))
    for item in sorted_data:
        total_profit = '{:.2f}'.format(item[2] * item[1])
        print(f"${total_profit} - {item[0]}/{item[1]}")

data = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        name, sales, profit = line.split()
        sales = int(sales)
        profit = float(profit)
        data.append((name, sales, profit))
    except EOFError:
        break
display_sorted_list(data)