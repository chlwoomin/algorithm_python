#1697
import sys
sys.setrecursionlimit(1000000)
def bfs(depth):
    i = len(queue)
    while i>0:
        q = queue.pop(0)
        if q == k:
            print(depth)
            return
        if visited[q] == True:
            i-=1
            continue
        visited[q] = True
        
        if q+1 <=k:
            queue.append(q+1)
        if q-1 >= 0:
            queue.append(q-1)
        if q*2 <= k*2:
            queue.append(q*2)
        i-=1
    bfs(depth+1)
n,k = map(int,input().split())
queue = [n]
visited = [False] * max((k*2+1),n+1)
bfs(0)