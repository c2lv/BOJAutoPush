import sys
input = lambda: sys.stdin.readline().rstrip()
import math

a, p1 = map(int, input().split())
r, p2 = map(int, input().split())

if a/p1 < math.pi*r*r/p2:
    print("Whole pizza")
else:
    print("Slice of pizza")