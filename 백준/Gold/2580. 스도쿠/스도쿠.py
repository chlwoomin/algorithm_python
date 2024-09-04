import sys
def dfs(y):
    global flag
    if flag == 1:
        return
    for i in range(y,9):
        for j in range(9):
            if testcase[i][j] == 0:
                intersection = set(row[i]) & set(col[j]) & set(square[i//3*3 + j//3])
                if len(intersection) == 1:
                    return
                for inter in intersection:
                    if flag==1:
                        return
                    if inter == False:
                        continue
                    testcase[i][j] = inter
                    row[i].remove(inter)
                    col[j].remove(inter)
                    square[i//3*3 + j//3].remove(inter)
                    dfs(i)
                    if flag==1:
                        return
                    row[i].append(inter)
                    col[j].append(inter)
                    square[i//3*3 + j//3].append(inter)
                    testcase[i][j] = 0
                return
    if flag == 0:
        flag=1
        for case in testcase:
            print(*case)
flag=0
cnt=0
testcase = [list(map(int,input().split())) for i in range(9)]
'''testcase=[[0, 3, 5, 0, 6, 9, 2, 7, 8],
            [7, 8, 2, 0, 0, 5, 6, 0, 9],
            [0, 6, 0, 2, 7, 8, 1, 3, 5],
            [3, 2, 0, 0, 4, 6, 8, 0, 7],
            [8, 0, 4, 9, 1, 3, 5, 0, 6],
            [5, 9, 6, 8, 2, 0, 4, 1, 3],
            [9, 1, 7, 6, 5, 2, 0, 8, 0],
            [6, 0, 3, 7, 0, 1, 9, 5, 2],
            [2, 5, 8, 0, 9, 4, 7, 6, 0]]'''
row = [[i for i in range(10)] for _ in range(9)]
col = [[i for i in range(10)] for _ in range(9)]
square = [[i for i in range(10)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        row[i][testcase[i][j]] = False
        col[i][testcase[j][i]] = False
for i in range(9):
    s_row = (i//3) * 3
    s_col = (i%3) * 3
    for j in range(3):
        for k in range(3):
            square[i][testcase[j+s_row][k+s_col]] = False
dfs(0)