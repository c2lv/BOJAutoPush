def print_star_pattern(n):
    if n == 3:
        pattern = ["***", "* *", "***"]
        return pattern

    prev_pattern = print_star_pattern(n // 3)
    pattern_size = n // 3
    pattern = []

    # 크기 N/3의 패턴으로 둘러싼 부분 그리기
    for line in prev_pattern:
        pattern.append(line * 3)
    for line in prev_pattern:
        pattern.append(line + " " * pattern_size + line)
    for line in prev_pattern:
        pattern.append(line * 3)

    return pattern


# 입력 받기
N = int(input())

# 패턴 출력
pattern = print_star_pattern(N)
for line in pattern:
    print(line)
