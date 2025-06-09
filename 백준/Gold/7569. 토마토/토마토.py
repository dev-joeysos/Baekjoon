from collections import deque
import sys
input=sys.stdin.readline
m,n,h=map(int,input().split())

box=[]
for _ in range(h):
    layer=[]
    for _ in range(n):
        layer.append(list(map(int,input().split())))
    box.append(layer)

def bfs(m,n,h,box):
    q=deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if box[z][y][x]==1:
                    q.append([z,y,x])
    dir=([1,0,0],[-1,0,0],[0,-1,0],[0,1,0],[0,0,1],[0,0,-1])
    
    while q:
        cz,cy,cx=q.popleft()
        for dz,dy,dx in dir:
            nz,ny,nx=cz+dz,cy+dy,cx+dx
            if 0<=nz<h and 0<=ny<n and 0<=nx<m:
                if box[nz][ny][nx]==0:
                    q.append([nz,ny,nx])
                    box[nz][ny][nx]=box[cz][cy][cx]+1        

bfs(m,n,h,box)
max_total=0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x]==0: #안익은 토마토가 있다면
                print(-1)
                sys.exit()
            elif box[z][y][x]>0:
                max_total=max(max_total,box[z][y][x])

print(max_total-1)