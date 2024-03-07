import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    students = list(input().split())
    mbti = {}
    for student in students:
        cases = [
            student,
            student[0] + student[1] + student[2],
            student[0] + student[1] + student[3],
            student[0] + student[2] + student[3],
            student[1] + student[2] + student[3],
            student[0] + student[1],
            student[0] + student[2],
            student[0] + student[3],
            student[1] + student[2],
            student[1] + student[3],
            student[2] + student[3],
            student[0],
            student[1],
            student[2],
            student[3]
        ]
        for case in cases:
            if case in mbti:
                mbti[case] += 1
            else:
                mbti[case] = 1
    max_len = 0
    for key, value in mbti.items():
        if value >= 3:
            max_len = max(len(key), max_len)
    print(8 - 2*max_len)