import sys
input = lambda: sys.stdin.readline().rstrip()

def back_tracking(now, end, sum, is_left):
    if now == end:
        if is_left:
            if sum in a1:
                a1[sum] += 1
            else:
                a1[sum] = 1
        else:
            if sum in a2:
                a2[sum] += 1
            else:
                a2[sum] = 1
    else:
        back_tracking(now+1, end, sum + a[now], is_left)
        back_tracking(now+1, end, sum, is_left)

n, s = map(int, input().split())
a = list(map(int, input().split()))
a1 = {}
a2 = {}
count = 0
back_tracking(0, n//2, 0, 1)
back_tracking(n//2, n, 0, 0)
a1 = [(num, count) for num, count in a1.items()]
a2 = [(num, count) for num, count in a2.items()]
a2.sort()
len_a2 = len(a2)
for t1 in a1:
    target = s - t1[0]
    left = 0
    right = len_a2
    while left < right:
        mid = (left+right)//2
        if a2[mid][0] < target:
            left = mid + 1
        else:
            right = mid
    if left < len_a2 and a2[left][0] == target:
        count += t1[1]*a2[left][1]
if s == 0:
    count -= 1
print(count)