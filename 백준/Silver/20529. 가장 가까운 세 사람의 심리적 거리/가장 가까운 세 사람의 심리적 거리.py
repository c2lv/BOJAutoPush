import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().split())
    if n > 32:
        print(0)
    else:
        same_len = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    same_len = max(
                        same_len,
                        (s[i][0] == s[j][0] == s[k][0])
                        + (s[i][1] == s[j][1] == s[k][1])
                        + (s[i][2] == s[j][2] == s[k][2])
                        + (s[i][3] == s[j][3] == s[k][3])
                    )
        print(8 - same_len*2)