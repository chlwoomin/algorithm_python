import sys
input = sys.stdin.readline

t = int(input())
cnt = 0
def bfs(x, y):
    global cnt
    if visited[y][x] == True:
        return
    queue = []
    queue.append([x, y])
    while queue:
        q = queue.pop()
        xx, yy = q[0], q[1]
        visited[yy][xx] = True
        for dx, dy in dxy_list:
            if xx + dx>=0 and xx + dx<m and yy + dy>=0 and yy + dy<n:
                if visited[yy + dy][xx + dx] == False and [xx + dx, yy + dy] in napaCabages:
                    queue.append([xx + dx, yy + dy])
    cnt += 1

dxy_list = [[0,1], [1,0], [0, -1], [-1, 0]]

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    napaCabages = [list(map(int, input().split())) for _ in range(k)]
    earthworm = 0
    visited = [[False] * m for _ in range(n)]
    for napaCabage in napaCabages:
        bfs(napaCabage[0], napaCabage[1])

    print(cnt)



