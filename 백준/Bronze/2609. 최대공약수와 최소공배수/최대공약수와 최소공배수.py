# 입력
n, m = map(int, input().split())

# a와 b의 최대 공약수를 리턴
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

g = gcd(n, m) # 최대 공약수
l = n * m // g # 최소 공배수
print(g)
print(l)