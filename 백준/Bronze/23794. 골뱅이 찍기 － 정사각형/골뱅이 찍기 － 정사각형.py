def square_at(n):
    for i in range(n+2):
        if i == 0 or i == n+1:
            print('@'*(n+2))
        else:
            print('@'+' '*n+'@')

square_at(int(input()))