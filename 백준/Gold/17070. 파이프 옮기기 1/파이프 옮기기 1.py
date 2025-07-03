# dp
import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dp=[[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0]=1
# dir=0,1,2(가로,세로,대각선)
for y in range(n):
    for x in range(n):
        for dir in range(3):
            if dp[y][x][dir]==0:
                continue
            #가로로 온 경우
            if dir==0 or dir==2:
                #가로 이동이 가능하면
                if x+1<n and graph[y][x+1]==0:
                    dp[y][x+1][0]+=dp[y][x][dir]
            #세로로 온 경우
            if dir==1 or dir==2:
                if y+1<n and graph[y+1][x]==0:
                    dp[y+1][x][1]+=dp[y][x][dir]
            #대각선으로 온 경우 (세 방향 모두 가능)
            if x+1<n and y+1<n:
                if graph[y][x+1]==0 and graph[y+1][x]==0 and graph[y+1][x+1]==0:
                    dp[y+1][x+1][2]+=dp[y][x][dir]
            
print(sum(dp[-1][-1]))