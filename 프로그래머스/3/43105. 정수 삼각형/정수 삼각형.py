def solution(triangle):
    answer = 0
    dp = [[0] * (i+1) for i in range(len(triangle))]
    for i, tri in enumerate(triangle):
        if i == 0:
            dp[i][0] = tri[0]
            continue
        for j, t in enumerate(tri):
            if j == 0:
                dp[i][j] = dp[i-1][j] + t
            elif j >= len(dp[i])-1:
                dp[i][j] = dp[i-1][j-1] +t
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + t
    answer = max(dp[i])
    return answer