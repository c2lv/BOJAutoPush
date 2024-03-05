n, m = map(int, input().split())
s = [input() for _ in range(n)]

can_build = 1
for i in range(n-1):
    is_dup = False
    for j in range(1, m+1):
        if s[i][:j] == s[i+1][m-j:] or s[i+1][:j] == s[i][m-j:]:
            is_dup = True
            break
    if not is_dup:
        can_build = 0
        break

print(can_build)