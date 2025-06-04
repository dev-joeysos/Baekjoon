dp = [0] * 1001
dp[1] = 1
dp[2] = 3

def tiling(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = (tiling(n - 1) + tiling(n - 2) * 2) % 10007
    return dp[n]

import sys
input = sys.stdin.readline
n = int(input())
print(tiling(n))
