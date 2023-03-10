import sys

s = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = int(sys.stdin.readline())
happiness_score = 1 * s + 2 * m + 3 * l
if happiness_score >= 10:
    print("happy")
else:
    print("sad")