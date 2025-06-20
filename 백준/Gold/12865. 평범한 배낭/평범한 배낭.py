#dp,knapsack
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
items=[list(map(int,input().split())) for _ in range(n)]

dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        #못넣는경우)i번째아이템무게>배낭무게j
        if items[i-1][0]>j:
            #=직전아이템까지 최대가치
            dp[i][j]=dp[i-1][j] 
        #넣는경우)
        else:
            #이전행값유지)넣을수있는데 안넣는게 더 나음
            opt1=dp[i-1][j]
            #넣고남은무게 최대가치+현재아이템가치)넣는게 더 나음
            w=j-items[i-1][0]#남은무게
            opt2=dp[i-1][w]+items[i-1][1]
            
            dp[i][j]=max(opt1,opt2)

#for row in dp:
#    print(row)
print(dp[-1][-1])