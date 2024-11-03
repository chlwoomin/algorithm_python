#2565
n = int(input())
line = [list(map(int,input().split())) for _ in range(n)]
#line = [[1,8],[3,9],[2,2],[4,1],[6,4],[10,10],[9,7],[7,6]]
line.sort()
result = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            result[i] = max(result[i], result[j]+1)
print(n - max(result))

