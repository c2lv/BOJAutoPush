value1, operation, value2 = input().split()

if operation == "AND":
    if value1 == "false" or value2 == "false":
        print("false")
    else:
        print("true")
else:
    if value1 == "true" or value2 == "true":
        print("true")
    else:
        print("false")