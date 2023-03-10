# 입력
n = int(input())
words = list(input() for _ in range(n))

'''
길이가 짧은 순, 길이가 같다면 사전 순으로 정렬
사전 순 정렬 이후 길이가 짧은 순으로 정렬된다.
'''
words.sort(key=lambda x:(len(x), x))

# 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력
before = '0' # 주어진 단어일 수 없는 단어
for word in words:
    if before == word:
        continue
    before = word
    print(word)