import sys
input = lambda: sys.stdin.readline().rstrip()

socks = {}
for _ in range(5):
    sock = input()
    if sock in socks.keys():
        socks[sock] += 1
    else:
        socks[sock] = 1
for sock in socks.keys():
    if socks[sock] % 2 == 1:
        print(sock)
        break