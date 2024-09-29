#2579
import sys
n = int(input())
stair = [int(sys.stdin.readline()) for _ in range(n)]
stair.insert(0,0)
dp = [[0,0] for _ in range(n+1)]
dp[0] = [0,0]
dp[1] = [stair[1],stair[1]]
for i in range(2,n+1):
    dp[i] = [stair[i]+dp[i-1][1], stair[i]+max(dp[i-2])]
print(max(dp[n]))