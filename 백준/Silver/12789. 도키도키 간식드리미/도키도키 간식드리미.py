#12789
n = int(input())
student = list(map(int,input().split()))
cnt = 1
stack = []
while len(student)>0:
    i = student.pop(0)
    try:
        if min(i,stack[len(stack)-1]) == cnt:
            j = stack.pop()
            if i > j:
                student.insert(0,i)
            else:
                stack.append(j)
            cnt+=1
        else:
            stack.append(i)
    except:
        if i == cnt:
            cnt+=1
        else:
            stack.append(i)
    try:
        if stack[len(stack)-1] > stack[len(stack)-2]:
            print("Sad")
            cnt = -1000
            break
    except:
        continue
cnt+=len(stack)-1
if cnt == n:
    print("Nice")
        