# DP
from collections import deque

n = int(input())
rgbTable = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]

dp[0] = rgbTable[0]

for i in range(n-1):
    dp[i+1][0] = min(dp[i][1], dp[i][2]) + rgbTable[i+1][0]
    dp[i+1][1] = min(dp[i][0], dp[i][2]) + rgbTable[i+1][1]
    dp[i+1][2] = min(dp[i][0], dp[i][1]) + rgbTable[i+1][2]

print(min(dp[-1]))