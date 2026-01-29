def bfs(queue, depth):
    while queue:
        next_queue = []
        while queue:
            z,y,x = queue.pop()
            for i,j,k in n_node:
                dz = z + i
                dy = y + j
                dx = x + k
                if in_tomato(dz,dy,dx) and tomato[dz][dy][dx] == 0:
                    tomato[dz][dy][dx] = 1
                    next_queue.append([dz,dy,dx])
        queue = next_queue
        depth += 1
    return depth

def in_tomato(z,y,x):
    if x>=0 and x < M and y>=0 and y< N and z>=0 and z < H:
        return True
    return False
def is_zero_in_tomato():
    for toma in tomato:
        for t in toma:
            if 0 in t:
                return True
    return False

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# z,y,x
n_node = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]

ripe_tomato = []
for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        for k in range(len(tomato[i][j])):
            if tomato[i][j][k] == 1:
                ripe_tomato.append([i,j,k])

res = bfs(ripe_tomato, 0)
if is_zero_in_tomato():
    print(-1)
else:
    print(res-1)
