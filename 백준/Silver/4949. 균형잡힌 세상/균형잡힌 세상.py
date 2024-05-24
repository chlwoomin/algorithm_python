#4949
stack = []
while True:
    stack.clear()
    s = input()
    if s == '.':
        break
    for i in s:
        try:
            if i == '.':
                if len(stack) == 0:
                    print("yes")
                else:
                    print("no")
                break
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if stack.pop() != '(':
                    print("no")
                    break
            elif i == ']':
                if stack.pop() != '[':
                    print("no")
                    break           
        except:
            print("no")
            break 