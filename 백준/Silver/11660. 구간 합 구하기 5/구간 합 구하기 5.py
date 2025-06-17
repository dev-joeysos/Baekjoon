import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [list(map(int, input().split())) for _ in range(m)]

# 누적합 dp 만들기 (1-indexed)
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = (
            dp[i-1][j] +
            dp[i][j-1] -
            dp[i-1][j-1] +
            grid[i-1][j-1]
        )

# 쿼리 처리
for y1, x1, y2, x2 in points:
    res = (
        dp[y2][x2] -
        dp[y1-1][x2] -
        dp[y2][x1-1] +
        dp[y1-1][x1-1]
    )
    print(res)