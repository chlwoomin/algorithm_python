#2156
import sys
n = int(input())
wine = [int(input()) for _ in range(n)]
wine.insert(0,0)
#wine = [0, 6, 10, 13, 9 , 8, 1]
dp = [[0,0,0] for _ in range(n+1)]
dp[1] = [wine[1],wine[1],wine[1]]
if n > 1:
    dp[2] = [wine[2],wine[2],wine[1] + wine[2]]
for i in range(3,n+1):
    dp[i] = [max(dp[i-3]) + wine[i], max(dp[i-2]) + wine[i], max(dp[i-1][0],dp[i-1][1]) + wine[i]]
print(max([max(dp[n]),max(dp[n-1])]))