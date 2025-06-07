import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

#initialize
INF=float('inf')
dist=[[INF]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            dist[i+1][j+1]=1
    
for k in range(1,n+1): #경유지
    for i in range(1,n+1): #출발지
        for j in range(1,n+1): #도착지
            if dist[i][k]!=INF and dist[k][j]!=INF:
                dist[i][j]=1

for row in dist[1:]:
    print(' '.join(str(x if x!=INF else 0) for x in row[1:]))