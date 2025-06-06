#헌내기는 친구가 필요해
from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[list(input().rstrip()) for _ in range(n)]
visited=[[False]*m for _ in range(n)]

#방문하지 않았고, 벽이 아닌 경우에만 이동 가능
def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    cnt=1 if board[x][y]=='P' else 0
    
    d=[(1,0),(0,1),(-1,0),(0,-1)]
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(board) and 0<=ny<len(board[0]):
                if not visited[nx][ny] and board[nx][ny]!='X':
                    visited[nx][ny]=True
                    if board[nx][ny]=='P':
                        cnt+=1
                    q.append((nx,ny))
            else:
                continue
    return cnt

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]=='I':
            result=bfs(i,j)
            print(result if result!=0 else 'TT')