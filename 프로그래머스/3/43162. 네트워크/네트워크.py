def solution(n, computers):
    global answer
    answer = 0
    visited = [False] * (n+1)
    # 0번은 제외 처리
    visited[0] = True
    for i in range(1, n+1):
        if visited[i] == False:
            bfs(i, computers, visited)
    return answer
def bfs(start, computers, visited):
    global answer
    queue = []
    queue.append(start)
    while queue:
        q = queue.pop()
        visited[q] = True
        for i, computer in enumerate(computers[q-1]):
            if visited[i+1] == False and computer == 1:
                queue.append(i+1)
    answer+=1
    
    
    