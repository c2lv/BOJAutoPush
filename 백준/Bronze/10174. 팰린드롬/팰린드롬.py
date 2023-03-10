t = int(input())
for _ in range(t):
    s = input()
    palindrome = True
    for i in range(len(s) // 2):
        a = ord(s[i])
        b = ord(s[len(s) - 1 - i])
        
        # 대문자는 소문자로 교체한 후 비교 
        if 65 <= a <= 90:
            a += 32
        if 65 <= b <= 90:
            b += 32

        if a != b:
            palindrome = False
            break
    if palindrome == True:
        print("Yes")
    else:
        print("No")