#dp, knapsack
import sys
input=sys.stdin.readline

def knapsack(c,ads):
    MAX=100_001
    dp=[0]*MAX # 비용 i로 확보 가능한 최대 고객 수

    for cost,custmers in ads:
        for i in range(cost,MAX):
            dp[i]=max(dp[i],dp[i-cost]+custmers)
    
    for i in range(MAX):
        if dp[i]>=c:
            print(i)
            break

def main():
    c,n=map(int,input().split())
    ads=[list(map(int,input().split())) for _ in range(n)]
    knapsack(c,ads)

if __name__=="__main__":
    main()