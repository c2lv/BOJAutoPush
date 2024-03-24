import sys
input = lambda: sys.stdin.readline().rstrip()

min = 500+1

def back_tracking(no):
    global min, n, s, team_start, team_link

    if no == n:
        start_ability = 0
        link_ability = 0
        for i in range(len(team_start)):
            for j in range(i, len(team_start)):
                start_ability += s[team_start[i]][team_start[j]] + s[team_start[j]][team_start[i]]
                link_ability += s[team_link[i]][team_link[j]] + s[team_link[j]][team_link[i]]
        if abs(start_ability - link_ability) < min:
            min = abs(start_ability - link_ability)
    else:
        if len(team_start) < n//2:
            team_start.append(no)
            back_tracking(no+1)
            team_start.pop()
        if len(team_link) < n//2:
            team_link.append(no)
            back_tracking(no+1)
            team_link.pop()

n = int(input())
team_start = []
team_link = []
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
back_tracking(0)
print(min)