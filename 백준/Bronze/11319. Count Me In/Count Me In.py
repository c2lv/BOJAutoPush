s = int(input())
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for _ in range(s):
    str = input()
    consonant_cnt = 0
    vowel_cnt = 0
    for char in str:
        if char in vowels:
            vowel_cnt += 1 
        elif char.isalpha(): # 모음이 아닌 알파벳은 자음
            consonant_cnt += 1
    print(consonant_cnt, vowel_cnt)