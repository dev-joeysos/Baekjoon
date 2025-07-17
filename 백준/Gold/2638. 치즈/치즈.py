# bfs: 외부공기 라운드마다 판별하기
from collections import deque
import sys
input=sys.stdin.readline

# 매 라운드마다 외부 공기인지, 내부 공기인지를 판별합니다.
def bfs_outer_air(grid):
    start_y,start_x=0,0
    directions=[(0,1),(-1,0),(0,-1),(1,0)]
    row=len(grid)
    col=len(grid[0])
    
    outer_air=[[False]*col for _ in range(row)]
    outer_air[start_y][start_x]=True
    q=deque()
    q.append((start_y,start_x))
    
    while q:
        cy,cx=q.popleft()
        
        for dy,dx in directions:
            ny=cy+dy
            nx=cx+dx
            if 0<=ny<row and 0<=nx<col:
                if outer_air[ny][nx]==False and grid[ny][nx]!=1:
                    outer_air[ny][nx]=True
                    q.append((ny,nx))
        
    return outer_air

# 그리드가 비었는지 판별합니다.
def is_empty_grid(grid):
    for row in grid:
        for block in row:
            if block==1:
                return False
    return True

# 최종 시간 계산
def cal_total_time(grid,n,m):
    dirs=[(0,1),(-1,0),(0,-1),(1,0)]
    total_time=0
    
    while True:
        if is_empty_grid(grid):
            break
        
        outer_air=bfs_outer_air(grid)
        new_grid=[row[:] for row in grid] #deepcopy
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    cnt=0
                    for di,dj in dirs:
                        ni,nj=i+di,j+dj
                        if 0<=ni<n and 0<=nj<m:
                            if grid[ni][nj]==0 and outer_air[ni][nj]:
                                cnt+=1
                    if cnt>=2:
                        new_grid[i][j]=0
        total_time+=1
        grid=[row[:] for row in new_grid]
    
    return total_time

def main():
    n,m=map(int,input().split())
    grid=[list(map(int,input().split())) for _ in range(n)]
    print(cal_total_time(grid,n,m))
    
if __name__=="__main__":
    main()