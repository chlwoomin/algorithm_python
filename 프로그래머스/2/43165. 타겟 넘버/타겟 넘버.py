def solution(numbers, target):
    global answer
    answer = 0
    n = len(numbers)
    dfs(target, numbers, 0, n)
    
    return answer

def dfs(target, numbers, depth, n):
    global answer
    if depth == n:
        if sum(numbers) == target:
            answer+=1
        return
    
    dfs(target, numbers, depth + 1, n)
    numbers[depth] = -numbers[depth]
    dfs(target, numbers, depth + 1, n)
    numbers[depth] = -numbers[depth]