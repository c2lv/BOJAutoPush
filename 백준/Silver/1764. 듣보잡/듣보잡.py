# 입력
n, m = map(int, input().split())
a = set(input() for _ in range(n))
b = set(input() for _ in range(m))

# 두 명단의 교집합(듣보잡)을 사전순으로 출력
c = list(a & b)
c.sort()

print(len(c))
for i in c:
    print(i)