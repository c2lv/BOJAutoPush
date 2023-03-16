import sys
input = sys.stdin.readline

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
dwarf_sum = sum(dwarf)
for i in range(8):
    for j in range(i + 1, 9):
        if dwarf_sum - dwarf[i] - dwarf[j] == 100:
            a = dwarf[i]
            b = dwarf[j]
            dwarf.remove(a)
            dwarf.remove(b)
            dwarf.sort()
            for d in dwarf:
                print(d)
            exit(0)