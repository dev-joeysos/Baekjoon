#このよからいっぴきのこらず
from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[list(map(int,input().strip())) for _ in range(n)]

q=deque([])
#[벽을 안 부수고 방문한 적이 있는지, 벽을 부수고 방문한 적이 있는지]
visited=[[[-1]*2 for _ in range(m)] for _ in range(n)]
dirs=[(1,0),(0,-1),(-1,0),(0,1)]
#시작점 기록
q.append((0,0,0))
visited[0][0][0]=1

#bfs
while q:
    cx,cy,break_the_wall=q.popleft()
    
    for dx,dy in dirs:
        nx=cx+dx
        ny=cy+dy
        # 다음 방향으로 전진이 가능하면
        if 0<=nx<n and 0<=ny<m:
            # 벽 아님(정상진입 가능)
            if board[nx][ny]==0 and visited[nx][ny][break_the_wall]==-1:
                visited[nx][ny][break_the_wall]=visited[cx][cy][break_the_wall]+1
                q.append((nx,ny,break_the_wall))
            # 벽이고+벽 부순적 없고+벽 부순상태로 다음 좌표에 간 적 없을 때
            elif board[nx][ny]==1 and break_the_wall==0 and visited[nx][ny][1]==-1:
                visited[nx][ny][1]=visited[cx][cy][break_the_wall]+1
                q.append((nx,ny,1)) #벽을 부수고 진입하겠다.

res1,res2=visited[n-1][m-1][0],visited[n-1][m-1][1]
if res1==-1 and res2==-1:
    print(-1)
elif res1==-1:
    print(res2)
elif res2==-1:
    print(res1)
else:
    print(min(res1,res2))