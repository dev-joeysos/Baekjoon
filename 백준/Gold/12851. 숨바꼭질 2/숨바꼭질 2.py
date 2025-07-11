#bfs
#최단 시간, 경로 수
from collections import deque
import sys
input=sys.stdin.readline

def bfs(start,end):
    limit=10**5+1
    #최단경로 시간
    visited=[-1]*limit
    visited[start]=0
    #최단경로 가짓수
    cnt=[0]*limit
    cnt[start]=1
    q=deque([start])
    
    while q:
        current=q.popleft()
        
        for next in [current-1,current+1,current*2]:
            if 0<=next<limit:
                if visited[next]==-1:
                    visited[next]=visited[current]+1
                    cnt[next]=cnt[current]
                    q.append(next)
                #이미 방문했는데, 같은 시간으로 또 도착할 수 있는 경우 최단경로 추가
                elif visited[next]==visited[current]+1:
                    cnt[next]+=cnt[current]
    
    return visited[end],cnt[end]

def main():
    n,k=map(int,input().split())
    t,c=bfs(n,k)
    print(t)
    print(c)
  
if __name__=="__main__":
    main()