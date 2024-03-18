import sys
input = lambda: sys.stdin.readline().rstrip()

gods = ["G","O","D"]
win = ["O","D","G"]
lose = ["D","G","O"]

t = int(input())
for _ in range(t):
    answer = "YES"
    answer_s = ""
    include = {"G": None, "O": None, "D": None} # 포함가능여부 체크
    inner = {"G": None, "O": None, "D": None}
    count = {"W": 0, "L": 0, "D": 0}
    gods_result = {"G": None, "O": None, "D": None}
    first = True

    n = int(input())
    god = input()
    wld = input()
    for i in range(n):
        count[wld[i]] += 1
        if god[i] == "?": # ? 패스
            continue
        if include[god[i]] == True and inner[god[i]] != wld[i]: # 이전에 나온 것과 다르면
            answer = "NO"
        include[god[i]] = True
        inner[god[i]] = wld[i]
        if first:
            idx = gods.index(god[i])
            if inner[god[i]] == "W":
                gods_result[god[i]] = "W"
                gods_result[win[idx]] = "L"
                gods_result[lose[idx]] = "X"
            elif inner[god[i]] == "L":
                gods_result[god[i]] = "L"
                gods_result[win[idx]] = "X"
                gods_result[lose[idx]] = "W"
            else:
                gods_result[god[i]] = "D"
                gods_result[win[idx]] = "D"
                gods_result[lose[idx]] = "D"
                # if n == 2:
                #     answer = "NO"
            first = False

    # if not ((count["D"] == n and n >= 3) or (count["W"] > 0 and count["L"] > 0 and count["D"] == 0)):
    if not ((count["D"] == n) or (count["W"] > 0 and count["L"] > 0 and count["D"] == 0)):
        answer = "NO"

    if first: # 전부 ?면
        if count["D"] == n:
            answer_s = "G"*n
        else:
            for i in range(n):
                if wld[i] == "W":
                    answer_s += "G"
                else:
                    answer_s += "O"
        if answer == "YES":
            print(answer)
            print(answer_s)
        else:
            print(answer)
        continue

    for i in range(n):
        if god[i] != "?":
            if gods_result[god[i]] == wld[i]:
                answer_s += god[i]
            else:
                answer = "NO"
        else:
            if count["D"] == n:
                if include["G"] == include["O"] == True:
                    answer_s += "D"
                elif include["G"] == include["D"] == True:
                    answer_s += "O"
                elif include["O"] == include["D"] == True:
                    answer_s += "G"
                else:
                    for key in gods:
                        if include[key] == True:
                            answer_s += key
            else:
                for key in gods_result.keys():
                    if wld[i] == gods_result[key]:
                        answer_s += key
                        break

    if answer == "YES":
            print(answer)
            print(answer_s)
    else:
        print(answer)