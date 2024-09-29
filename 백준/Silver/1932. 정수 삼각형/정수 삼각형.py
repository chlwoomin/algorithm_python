#1932
import sys
n = int(input())
triangle = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

sum_max = [[0 for _ in range(i+1)] for i in range(n)]
sum_max[0][0] = triangle[0][0]
for i in range(1,n):
    for j in range(i):
        sum_max[i][j] = max(sum_max[i-1][j] + triangle[i][j], sum_max[i][j])
        sum_max[i][j+1] = max(sum_max[i-1][j] + triangle[i][j+1], sum_max[i][j+1])
print(max(sum_max[n-1]))