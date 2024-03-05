t = int(input())
for _ in range(t):
    n = input()
    print("Good") if (int(n) + 1) % int(n[2:]) == 0 else print("Bye")