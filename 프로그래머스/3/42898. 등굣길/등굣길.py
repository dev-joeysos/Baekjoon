def solution(m, n, puddles):
    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[1][1] = 1
    
    for puddle in puddles:
        dp[puddle[0]][puddle[1]] = -1
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            if i > 1: 
                dp[i][j] += dp[i-1][j]
            if j > 1:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= 1000000007
    return dp[m][n] 