#11053
n = int(input())
A = list(map(int,input().split()))
#A = [1, 3, 2, 3]
sorted_A = sorted(set(A))
A_index = [[] for _ in range(max(A) + 1)]
dp = [0] * (n+2)
for i in range(len(A)):
    A_index[A[i]].append(i+1)
for i in sorted_A:
    for j in sorted(A_index[i],reverse=True):
        dp[j] = max(dp[:j]) + 1
print(max(dp))