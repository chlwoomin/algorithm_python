#11725
from collections import deque
import sys
def bfs(rootnode):
    queue = deque([rootnode])
    visited[rootnode] = True
    
    while queue:
        node = queue.popleft()
        
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                answer[i] = node

n = int(sys.stdin.readline())
visited = [False] * (n+1)
answer = [list() for i in range(n+1)]
graph = [list() for i in range(n+1)]
arr = [list(map(int,sys.stdin.readline().split())) for i in range(n-1)]
for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
bfs(1)
for i in answer:
    if i == []: continue
    print(i)


