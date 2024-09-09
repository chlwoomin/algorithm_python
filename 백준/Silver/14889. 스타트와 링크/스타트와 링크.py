#14889
import sys
def dfs(depth,start):
    global n#,cnt
    if depth == 0:
        s1=0
        s2=0
        team2 = list(set(member) - set(team1))
        for i in range(len(team1)):
            for j in range(i+1,len(team1)):
                #cnt+=1
                s1 += score[team1[i]][team1[j]]
        for i in range(len(team2)):
            for j in range(i+1,len(team2)):
                s2 += score[team2[i]][team2[j]]
        minimum.append(abs(s1-s2))
        return
    
    for i in range(start,n):
        if depth == n//2 and i != 0:
            return
        if i in team1:
            continue
        team1.append(i)
        dfs(depth-1,i)
        team1.remove(i)
        
minimum = []
team1 = []
team2 = []
#cnt = 0
n= int(input())
member = [i for i in range(n)]
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
'''board = [[0,1, 2, 3, 4, 5],
            [1, 0, 2, 3, 4, 5],
            [1, 2, 0, 3, 4, 5],
            [1, 2, 3, 0, 4, 5],
            [1, 2, 3, 4, 0, 5],
            [1, 2, 3, 4, 5, 0]]'''
score = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i,n):
        score[i][j] = board[i][j]+board[j][i]
dfs(n//2,0)
print(min(minimum))