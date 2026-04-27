import sys
input = sys.stdin.readline

MIN_MAX = 10**9 * 2
n = int(input())
nums = list(map(int, input().split()))
left, right = 0, n-1
min_sum = MIN_MAX
min_left, min_right = 0, n-1
while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == 0:
        min_left, min_right = left, right
        break
    if abs(current_sum) < abs(min_sum):
        min_sum = current_sum
        min_left, min_right = left, right
    if nums[left] + nums[right] < 0:
        left += 1
    else:
        right -= 1
print(nums[min_left], nums[min_right])