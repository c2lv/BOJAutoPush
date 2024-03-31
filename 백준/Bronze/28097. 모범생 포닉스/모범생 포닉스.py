n = int(input())
t = list(map(int, input().split()))
day = ((n-1)*8 + sum(t)) // 24
hour = ((n-1)*8 + sum(t)) % 24
print(day, hour)