kda = input()
kda_list = kda.split(sep='/')
k = int(kda_list[0])
d = int(kda_list[1])
a = int(kda_list[2])
if k + a < d or d == 0:
    print('hasu')
else:
    print('gosu')