import sys,math
input=sys.stdin.readline

def is_sq(n):
    return True if int(math.sqrt(n))**2==n else False

n=int(input())
dp=[0]*(n+1)

for i in range(1,n+1):
    if is_sq(i):
        dp[i]=1
        continue
    else: #제곱수가 아니라면
        dp[i]=min(dp[i-j**2]+1 for j in range(1,int(math.sqrt(i))+1))

print(dp[n])