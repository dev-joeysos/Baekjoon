from collections import deque
import sys

def bfs(n,grid):
    q=deque()
    visited=[[False]*n for _ in range(n)]
    dir=([0,1],[0,-1],[1,0],[-1,0])
    total=0
    for j in range(n):
        for i in range(n):
            if not visited[j][i]:
                total+=1 #새로운 구역을 탐색하기 시작할 때 구역 수 증가
                q.append([j,i])
                visited[j][i]=True
                while q:
                    cy,cx=q.popleft()
                    for dy,dx in dir:
                        ny,nx=cy+dy,cx+dx
                        #방문하지 않았고, 현재 색상과 동일하다면
                        if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and grid[ny][nx]==grid[cy][cx]:
                            visited[ny][nx]=True
                            q.append([ny,nx])
    return total

#입력
input=sys.stdin.readline
n=int(input())
grid=[list(input().strip()) for _ in range(n)]

#입력처리
blind_grid=[row[:] for row in grid]
for j in range(n):
    for i in range(n):
        if blind_grid[j][i]=='G':
            blind_grid[j][i]='R'

#출력
print(bfs(n,grid), bfs(n,blind_grid))