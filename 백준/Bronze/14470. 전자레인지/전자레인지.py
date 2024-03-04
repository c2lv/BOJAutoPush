a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

time = 0
if a < 0:
    time += (-a*c) + d + b*e
else:
    time += (b-a)*e
print(time)