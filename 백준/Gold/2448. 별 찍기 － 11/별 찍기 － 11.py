def star_stamp(n):
    if n == 3:
        return [
            "  *   ",
            " * *  ",
            "***** "
        ]
    before = star_stamp(n//2)
    line = []
    for b in before:
        line.append(" "*(n//2) + b + " "*(n//2))
    for b in before:
        line.append(2*b)
    return line

n = int(input())
lines = star_stamp(n)
for line in lines:
    print(line)