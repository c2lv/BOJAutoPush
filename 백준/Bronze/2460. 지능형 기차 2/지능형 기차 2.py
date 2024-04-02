import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(train):
    now = 0
    answer = 0
    for i in range(10):
        now += train[i][1] - train[i][0]
        if now > answer:
            answer = now
    return answer

train = []
for i in range(10):
    train.append(tuple(map(int, input().split())))
print(solve(train))