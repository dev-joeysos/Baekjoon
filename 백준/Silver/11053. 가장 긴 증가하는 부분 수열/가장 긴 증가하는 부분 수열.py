# LIS_DP
n = int(input())
sequence = list(map(int, input().split()))

dp = [0*i for i in range(n)]

for i in range(n):
    dp[i] = 1
    for j in range(i):
        # 현재 숫자가 앞 숫자보다 큰 경우에만 비교한다
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))