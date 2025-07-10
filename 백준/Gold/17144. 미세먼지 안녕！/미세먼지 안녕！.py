'''
미세먼지 안녕!

t초가 지난 후 남아있는 방의 미세먼지 양 출력

'''
import sys
input=sys.stdin.readline

# 미세먼지 확장
def spread(grid):
    new_grid=[row[:] for row in grid]
    direcions=[(0,1),(-1,0),(0,-1),(1,0)]
    row=len(new_grid)
    col=len(new_grid[0])
    
    for y in range(row):
        for x in range(col):
            if grid[y][x]!=0 and grid[y][x]!=-1:
                spread_amount=grid[y][x]//5
                spread_count=0
                for dy,dx in direcions:
                    ny,nx=y+dy,x+dx
                    if 0<=ny<row and 0<=nx<col:
                        if grid[ny][nx]!=-1:
                            new_grid[ny][nx]+=spread_amount
                            spread_count+=1
                new_grid[y][x]-=spread_amount*spread_count
    
    return new_grid

# 청정기의 (y,x) 좌표 반환
def find_cleaner(grid):
    row=len(grid)
    col=len(grid[0])
    air_pos=[]
    
    for y in range(row):
        for x in range(col):
            if grid[y][x]==-1:
                air_pos.append((y,x))
    return air_pos

# 반시계(위쪽) 정화
def purify_upper(grid, air_pos):
    R, C = len(grid), len(grid[0])
    y, _ = air_pos[0]
    new_grid = [row[:] for row in grid]

    # 1) 정화기 행 → 오른쪽
    for x in range(1, C):
        new_grid[y][x] = grid[y][x-1]
    # 2) 오른쪽 끝 열 ↑ 위로
    for i in range(y-1, -1, -1):
        new_grid[i][C-1] = grid[i+1][C-1]
    # 3) 맨 위 행 ← 왼쪽
    for x in range(C-2, -1, -1):
        new_grid[0][x] = grid[0][x+1]
    # 4) 왼쪽 끝 열 ↓ 아래로
    for i in range(1, y+1):
        new_grid[i][0] = grid[i-1][0]

    # 정화 위치 마무리
    new_grid[y][1] = 0
    new_grid[y][0] = -1
    return new_grid

# 시계(아래쪽) 정화
def purify_lower(grid, air_pos):
    R, C = len(grid), len(grid[0])
    y, _ = air_pos[1]
    new_grid = [row[:] for row in grid]

    # 1) 정화기 행 → 오른쪽
    for x in range(1, C):
        new_grid[y][x] = grid[y][x-1]
    # 2) 오른쪽 끝 열 ↓ 아래로
    for i in range(y+1, R):
        new_grid[i][C-1] = grid[i-1][C-1]
    # 3) 맨 아래 행 ← 왼쪽
    for x in range(C-2, -1, -1):
        new_grid[R-1][x] = grid[R-1][x+1]
    # 4) 왼쪽 끝 열 ↑ 위로
    for i in range(R-2, y-1, -1):
        new_grid[i][0] = grid[i+1][0]

    # 정화 위치 마무리
    new_grid[y][1] = 0
    new_grid[y][0] = -1
    return new_grid

# 미세먼지 양 계산
def count_dust(grid):
    new_grid=[row[:] for row in grid]
    row=len(grid)
    col=len(grid[0])
    total=0
    
    for y in range(row):
        for x in range(col):
            if grid[y][x]==-1:
                continue
            total+=grid[y][x]
            
    return total
        
def main():
    r,c,t=map(int,input().split())
    grid=[list(map(int,input().split())) for _ in range(r)]
    air_pos=find_cleaner(grid)
   
    for _ in range(t):
        spreaded_grid=spread(grid)
        grid=purify_lower(purify_upper(spreaded_grid,air_pos),air_pos)

    print(count_dust(grid))

if __name__=="__main__":
    main()