b=input()
al=['c=','c-','dz=','d-','lj','nj','s=','z=']
sum = len(b)
cnt = 0
for i in al:
    cnt = b.count(i)
    sum -= cnt
print(sum)