sum, difference = map(int, input().split())
team1 = sum + difference
if team1 % 2 == 1:
    print(-1)
else:
    team1 //= 2
    team2 = sum - team1
    if team2 < 0:
        print(-1)
    elif team1 > team2:
        print(team1, team2)
    else:
        print(team2, team1)