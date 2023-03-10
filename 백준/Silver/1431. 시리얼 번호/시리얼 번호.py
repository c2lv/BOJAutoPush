n = int(input())

guitars = list(list(input()) for _ in range(n))

# 사전 순 오름차순으로 정렬
guitars.sort(key=lambda x:x)

# 자리수의 합 오름차순으로 정렬
def intsum(a):
    result = 0
    for i in a:
        if 48 <= ord(i) <= 57:
            result += ord(i) - 48
    return result

guitars.sort(key=lambda x:intsum(x))

# 짧은 순으로 정렬
guitars.sort(key=lambda x:len(x))

for guitar in guitars:
    for i in range(len(guitar)):
        print(guitar[i], end='')
    print()