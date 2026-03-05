def solution(n, w, num):
    stacks = [[] for _ in range(w)]
    for i in range(n):
        #i+1번째 값을 각 위치에 맞는 스택에 삽입
        if i//w % 2 == 0:
            stacks[i%w].append(i+1)
        else:
            stacks[-(i%w+1)].append(i+1)
    for stack in stacks:
        if num in stack:
            answer = len(stack) - stack.index(num)
            break
    return answer