#2178
import sys
sys.setrecursionlimit(100000)
def bfs(depth):
    global answer
    i = len(queue)
    while i>0:
        x,y = queue.pop(0)
        
        for dx,dy in v:
            if x+dx == n-1 and y+dy == m-1:
                answer = depth
                return 
            if 0<=x+dx<n and 0<=y+dy<m and visited[x+dx][y+dy] == False and graph[x+dx][y+dy] == 1:
                visited[x+dx][y+dy] = True
                queue.append([x+dx,y+dy])
        i -=1
    bfs(depth+1)
n,m = map(int,input().split())
graph = [[0]*m for _ in range(n)]
for i in range(n):
    a = input()
    for j in range(m):
        graph[i][j] = int(a[j])
visited = [[False]*m for _ in range(n)]
visited[0][0] = True
v = [[0,1],[0,-1],[1,0],[-1,0]]
queue = [[0,0]]
bfs(1)
print(answer+1)