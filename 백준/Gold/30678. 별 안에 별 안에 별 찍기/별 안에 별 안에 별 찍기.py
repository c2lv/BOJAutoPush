def star(i):
    if i == 0:
        return ['*']
    else:
        space_width = 5**(i-1)
        pattern = []
        row = star(i - 1)*5
        for j in range(5**i):
            if j < 5**(i-1):
                pattern.append(' '*2*space_width+row[j]+' '*2*space_width)
            elif j < 5**(i-1)*2:
                pattern.append(' '*2*space_width+row[j]+' '*2*space_width)
            elif j < 5**(i-1)*3:
                pattern.append(row[j]*5)
            elif j < 5**(i-1)*4:
                pattern.append(' '*space_width+row[j]*3+' '*space_width)
            else:
                pattern.append(' '*space_width+row[j]+' '*space_width+row[j]+' '*space_width)
        return pattern

n = int(input())
for row in star(n):
    print(row)