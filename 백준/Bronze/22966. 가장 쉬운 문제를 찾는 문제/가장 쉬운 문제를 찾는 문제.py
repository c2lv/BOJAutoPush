n = int(input())
easiest_name = ''
easiest_level = 5
for _ in range(n):
    name, level = input().split()
    level = int(level)
    if level < easiest_level:
        easiest_name = name
        easiest_level = level
    elif level == easiest_level:
        for i in range(len(name)):
            if ord(name[i]) < ord(easiest_name[i]):
                easiest_name = name
                easiest_level = level
                break
            elif ord(name[i]) > ord(easiest_name[i]):
                break
print(easiest_name)