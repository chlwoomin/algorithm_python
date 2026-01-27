from itertools import combinations
n, k = map(int,input().split())
dp = [[0] * (n+ 1) for _ in range(k+1)]
for i in range(1, k+1): # i: 선택 개수
    for num in range(0, n+1): # num: 완성할 수
        if i == 1:
            dp[i][num] = 1
            continue
        dp[i][num] = sum(dp[i-1][:num+1])
print(dp[k][n] % 1000000000)