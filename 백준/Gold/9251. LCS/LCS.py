#태그: dp,lcs(longest common subsequence)
import sys
input=sys.stdin.readline
t1=input().strip()
t2=input().strip()
n,m=len(t1),len(t2)
dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        # 공통의 문자라면 t1,t2에서 하나씩 빠진, 직전 부분 순열의 최대길이+1
        if t1[i-1]==t2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        # 다르다면 t1,t2 중 하나씩 뺀 직전 문자열 중 하나에 저장된 값 중 하나
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])