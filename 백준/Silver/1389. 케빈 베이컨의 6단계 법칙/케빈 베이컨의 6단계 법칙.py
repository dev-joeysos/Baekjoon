#케빈베이컨
#플로이드워셜
from collections import defaultdict,deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    x,y=map(int,input().split())
    d[x].append(y)
    d[y].append(x)

def bfs(k,n,d): #n=유저 수
    q=deque()
    visited=[False]*(n+1)
    total=0
    q.append((k,0))
    visited[k]=True
    
    while q:
        cn,dist=q.popleft()
        for i in d[cn]:
            if not visited[i]:
                total+=dist+1
                visited[i]=True
                q.append((i,dist+1))

    return total

distance=[0]*(n+1)
for i in range(1,n+1):
    distance[i]=bfs(i,n,d)
    
print(distance[1:].index(min(distance[1:]))+1)