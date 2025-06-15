#dp
import sys
input=sys.stdin.readline
n=int(input())
dp=[list(map(int,input().split())) for _ in range(n)]

#print(dp)
for i in range(1,len(dp)): #첫 줄은 생략
    for j in range(len(dp[i])):
        if j==0: #좌측 끝
            dp[i][j]+=dp[i-1][j]
        elif j==len(dp[i])-1: #우측 끝
            dp[i][j]+=dp[i-1][j-1]
        else: #가운데
            dp[i][j]+=max(dp[i-1][j-1],dp[i-1][j])

max_val=0
for i in dp[n-1]: #그래프 최하단
    max_val=max(max_val,i)

print(max_val)