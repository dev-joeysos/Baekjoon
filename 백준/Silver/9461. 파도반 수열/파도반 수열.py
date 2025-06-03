import sys
input=sys.stdin.readline

dp=[0]*101
dp[0],dp[1],dp[2]=1,1,1

def padovan(n):
    if dp[n]:
        return dp[n]
    dp[n]=padovan(n-2)+padovan(n-3)
    return dp[n]

T=int(input())
for _ in range(T):
    print(padovan(int(input())-1))