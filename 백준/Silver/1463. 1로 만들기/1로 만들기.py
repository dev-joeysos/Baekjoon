# 바텀 업의 풀이 클론 코딩
n = int(input())
dp = [0]*(n+1)  # d에 계산된 값을 저장해둔다.
# 점화식
# dp[i] = min(dp[i-1]+1, dp[i//2]+1, dp[i//3]+1)

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])