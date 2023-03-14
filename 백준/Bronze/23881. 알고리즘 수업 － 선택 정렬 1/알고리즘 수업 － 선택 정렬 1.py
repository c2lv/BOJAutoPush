# a를 오름차순 정렬한다.
def selection_sort(a, k):
    for last in range(n - 1, 0, -1):
        # a[1..last] 중 가장 큰 수 a[i]를 찾는다
        max_value = max(a[:last + 1])
        i = a.index(max_value)
        # last와 i가 서로 다르면 a[last]와 a[i]를 교환
        if last != i:
            temp = a[i]
            a[i] = a[last]
            a[last] = temp
            k -= 1
            if k == 0:
                print(a[i], a[last])
                break
    if k != 0:
        print(-1)

n, k = map(int, input().split())
a = list(map(int, input().split()))
selection_sort(a, k)