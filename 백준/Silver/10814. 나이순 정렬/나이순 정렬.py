import sys

n = int(sys.stdin.readline())
members = []
for i in range(n):
    members.append(sys.stdin.readline().split())
    members[i].append(i)

# 가입한 순으로 정렬
members.sort(key=lambda x: x[2])
# 나이 순으로 정렬
members.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(members[i][0], members[i][1])