#dfs,bitmasking,backtracking
import sys
input=sys.stdin.readline

def dfs(y,x,visited,depth):
    directions=[(1,0),(0,-1),(-1,0),(0,1)]
    global answer
    answer=max(answer,depth)
    
    for dy,dx in directions:
        ny=y+dy
        nx=x+dx
        #방문 가능한 범위에 속하고
        if 0<=ny<r and 0<=nx<c:
            idx=ord(grid[ny][nx])-ord('A')
            #방문했던 알파벳인 경우(전진불가)
            if visited & (1<<idx):
                continue
            #방문하지 않았던 알파벳인 경우(전진가능)
            dfs(ny,nx,visited|1<<idx,depth+1)

r,c=map(int,input().split())
grid=[]
for _ in range(r):
    grid.append(list(input().strip()))

visited=0
start_bit=ord(grid[0][0])-ord('A')
visited=(1<<start_bit)
        
answer=1
dfs(0,0,visited,1)
print(answer)