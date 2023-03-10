while True:
    n = int(input())
    if n == -1:
        break
    result = 1
    s = str(n) + " = " + "1"
    for i in range(1, n - 1):
        if n % (i + 1) == 0:
            result += i + 1
            s = s + " + " + str(i + 1)
    if n == result:
        print(s)
    else:
        print(f"{str(n)} is NOT perfect.")