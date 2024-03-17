import sys
input = lambda: sys.stdin.readline().rstrip()

infix = input()
operator = []
postfix = ""
before_op = 0
parentheses = []

for c in infix:
    if c == "(":
        before_op = 0
        parentheses.append(0)
    elif c == ")":
        temp = parentheses.pop()
        while temp > 0:
            postfix += operator.pop()
            temp -= 1
        if operator:
            if operator[-1] in "+-":
                before_op = 1
            else:
                before_op = 2
        else:
            before_op = 0
    elif c in "+-":
        if before_op >= 1:
            if parentheses:
                while parentheses[-1] > 0:
                    postfix += operator.pop()
                    parentheses[-1] -= 1
            else:
                while operator:
                    postfix += operator.pop()
        operator.append(c)
        before_op = 1
        if parentheses:
            parentheses[-1] += 1
    elif c in "*/":
        if before_op == 2:
            if parentheses:
                while parentheses[-1] > 0 and operator[-1] in "*/":
                    postfix += operator.pop()
                    parentheses[-1] -= 1
            else:
                while operator and operator[-1] in "*/":
                    postfix += operator.pop()
        operator.append(c)
        before_op = 2
        if parentheses:
            parentheses[-1] += 1
    else:
        postfix += c
while operator:
    postfix += operator.pop()
print(postfix)