# floyd = 3중 dp
from collections import defaultdict
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())

INF=float('inf')
dist=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dist[i][i]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    dist[a][b]=min(dist[a][b],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            #만약 거쳐 가는 경로가 더 짧으면 갱신
            if dist[i][j]>dist[i][k]+dist[k][j]:
                dist[i][j]=dist[i][k]+dist[k][j]
            #아니면 계속 돌기
            else:
                continue

for row in dist[1:]:
    print(' '.join(str(i) if i!=INF else '0' for i in row[1:]))