#목표지점까지의 최단거리 구하기
from collections import deque

def bfs(graph,x,y,result):
    n,m=len(graph),len(graph[0])
    visited=[[False]*m for _ in range(n)]
    visited[x][y]=True
    result[x][y]=0
    q=deque()
    q.append((x,y)) #current position
    
    while q:
        cx,cy=q.popleft()
        for dx,dy in [(1,0),(0,-1),(-1,0),(0,1)]:
            nx,ny=cx+dx,cy+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]==1:
                visited[nx][ny]=True
                result[nx][ny]=result[cx][cy]+1
                q.append((nx,ny))

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

result=[[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            bfs(graph,i,j,result)

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(0, end=' ')
        elif result[i][j]==-1:
            print(-1, end=' ')
        else:
            print(result[i][j],end=' ')
    print()