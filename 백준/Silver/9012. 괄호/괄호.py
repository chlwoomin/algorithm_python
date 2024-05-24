#9012
t = int(input())
stack = []
for i in range(t):
    ps = input()
    for j in ps:
        if j == '(':
            stack.append('(')
        else:
            if len(stack)!=0:
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
    stack.clear()