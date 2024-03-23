#4963
import sys
sys.setrecursionlimit(10000)
def dfs(x,y,island,visited):
    visited[y][x] = True
    if island[y][x] == 0:
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            next_x = x+j-1
            next_y = y+i-1
            if next_x < w and next_y < h and next_x >= 0 and next_y >= 0:
                if not visited[next_y][next_x]:
                    if island[next_y][next_x] == 1:
                        dfs(next_x,next_y,island,visited)

while True:
    w, h =map(int,input().split())
    if w == 0 and h == 0:
        break
    island = []
    #visited = [[False]*w]*h 얕은복사
    visited = [[False] * w for i in range(h)] 
    cnt=0

    for i in range(h):
        island.append(list(map(int,input().split())))
    for y in range(h): # y: 세로축
        for x in range(w): # x: 가로축
            if visited[y][x] == False:
                if island[y][x] == 1:
                    dfs(x,y,island,visited)
                    cnt+=1
                else:
                    visited[y][x] = True
    print(cnt)