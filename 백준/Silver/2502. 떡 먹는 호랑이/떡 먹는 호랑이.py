def get_ab_coefficient(d):
    a = 0
    b = 1
    for _ in range(d-2):
        c = a + b
        a = b
        b = c
    return a, b

d, k = map(int, input().split())
a_coe, b_coe = get_ab_coefficient(d)
a = 1
while True:
    if (k - a_coe * a) % b_coe == 0:
        b = (k - a_coe * a) // b_coe
        break
    a += 1
print(a)
print(b)