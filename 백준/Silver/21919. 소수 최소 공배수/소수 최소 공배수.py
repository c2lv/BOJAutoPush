import sys, math
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
# 같은 수 중복을 방지하기 위해 딕셔너리 자료형 사용
b = defaultdict(int)
result = 1

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(0, len(a)):
    if is_prime_number(a[i]):
       b[a[i]] += 1 

for prime_number in b.keys():
    result *= prime_number

if result == 1: # 수열 a의 원소 중 소수가 없을 경우
    print(-1)
else:
    print(result)