def max_profit(a):
    if not a or len(a) < 2:
        return 0
    
    max_profit = 0
    min_price = a[0]
    
    for price in a:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
        
    return max_profit

t = int(input())
a = list(map(int, input().split()))
result = max_profit(a)
print(result)
