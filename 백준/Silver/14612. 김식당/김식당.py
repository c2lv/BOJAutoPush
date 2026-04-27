n, m = map(int, input().split())
postits = [] # (table number, order time)
for _ in range(n):
    command, *args = input().split()
    
    if command == "order":
        postits.append((int(args[0]), int(args[1])))
    elif command == "sort":
        postits.sort(key=lambda x: (x[1], x[0]))
    elif command == "complete":
        postits = [x for x in postits if x[0] != int(args[0])]
    
    if postits:
        for postit in postits:
            print(postit[0], end=" ")
        print()
    else:
        print("sleep")