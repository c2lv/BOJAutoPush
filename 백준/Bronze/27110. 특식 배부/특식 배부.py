n = int(input())
abc = list(map(int, input().split()))
result = 0
for i in abc:
    if i <= n:
        result += i
    else:
        result += n
print(result)