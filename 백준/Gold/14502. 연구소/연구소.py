'''
bfs
'''
from collections import deque
import sys
input=sys.stdin.readline

def bfs(grid):
    n=len(grid)
    m=len(grid[0])
    directions=[(0,1),(-1,0),(1,0),(0,-1)]
    q=deque()
    domain=0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                q.append((i,j))
                
    while q:
        y,x=q.popleft()
        
        for dy,dx in directions:
            ny=y+dy
            nx=x+dx
            if 0<=ny<n and 0<=nx<m:
                if grid[ny][nx]!=1 and grid[ny][nx]!=2:
                    grid[ny][nx]=2
                    q.append((ny,nx))
                    
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                domain+=1
    
    return domain    

def build_wall(grid):
    n=len(grid)
    m=len(grid[0])
    max_val=-1
    for i in range(n*m-2):
        yi,xi=i//m,i%m
        if grid[yi][xi]!=0:
            continue
        
        for j in range(i+1,n*m-1):
            yj,xj=j//m,j%m
            if grid[yj][xj]!=0:
                continue
                
            for k in range(j+1,n*m):
                yk,xk=k//m,k%m
                if grid[yk][xk]!=0:
                    continue
                
                new_grid=[row[:] for row in grid]
                new_grid[yi][xi],new_grid[yj][xj],new_grid[yk][xk]=1,1,1
                max_val=max(max_val,bfs(new_grid))
    
    return max_val

def main():
    n,m=map(int,input().split())
    grid=[list(map(int,input().split())) for _ in range(n)]
    print(build_wall(grid))
    
if __name__=="__main__":
    main()