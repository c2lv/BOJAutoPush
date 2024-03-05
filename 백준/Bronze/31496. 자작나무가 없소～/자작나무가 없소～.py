n, s = input().split()
item = {}
answer = 0
for _ in range(int(n)):
    name, value = input().split()
    item[name] = int(value)
for key in item.keys():
    split_key = key.split(sep="_")
    if s in split_key:
        answer += item[key]
print(answer)