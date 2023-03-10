n, k = map(int, input().split())
def bin_coe(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    elif k == 0 or n == k:
        return 1
    else:
        return bin_coe(n - 1, k - 1) + bin_coe(n - 1, k)
print(bin_coe(n, k))