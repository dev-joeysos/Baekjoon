import sys
n = int(sys.stdin.readline())

def fiboDP(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    if n > 0:
        dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print(fiboDP(n))