import sys
input = sys.stdin.readline

lcm = lambda a, b: a * b // gcd(a, b) # 최대공약수
gcd = lambda a, b: a if not b else gcd(b, a % b) # 최소공배수

a, b = map(int, input().split())
print(lcm(a, b))