N, L = map(int, input().split())
location = list(map(int, input().split()))
tape = 0
count = 0

for i in range(1, 1001):
    if 0 < tape:
        tape -= 1
        continue
    if i in location:
        tape = L - 1
        count += 1

print(count)


'''
쉽게 생각하면 그냥 N을 L로 나눈 값을 올림하면 됨
그런데 테이프는 자를 수 없으므로 이걸 처리하는 게 관건
어차피 테이프는 물이 새는 곳이 보이면 바로 붙여야 됨
그 때 1 카운트하고
그 뒤로는 테이프 길이만큼 테이프가 붙어 있을 테니까 체크하지 말고 테이프 길이만큼 패스하자
카운트한 만큼 출력하면 될 듯
'''