import sys
input = lambda: sys.stdin.readline().rstrip()

def decrease_num(n):
    dp = [[[] for _ in range(10)] for _ in range(11)]
    for i in range(11):
        for j in range(i-1, 10):
            if i == 0:
                continue
            if i == 1:
                dp[i][j] = [str(j)]
                if n == 0:
                    return str(j)
                n -= 1
            else:
                for k in range(j):
                    for e in dp[i-1][k]:
                        dp[i][j].append(str(j)+e)
                        if n == 0:
                            return str(j)+e
                        n -= 1
    return -1
n = int(input())
print(decrease_num(n))