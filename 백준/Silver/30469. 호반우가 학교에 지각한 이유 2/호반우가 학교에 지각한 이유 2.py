a, b, n = input().split()
start = a[1]
end = b[0]
if int(end) in [1, 3, 7, 9]:
    if int(start) in [1, 3, 7]:
        print(a+'1'*(int(n)-4)+b)
    elif int(start) == 9:
        print(a+'7'+'1'*(int(n)-5)+b)
    else:
        print(-1)
else:
    print(-1)