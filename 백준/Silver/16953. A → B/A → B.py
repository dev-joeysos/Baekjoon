from collections import deque
import sys
input=sys.stdin.readline
a,b=map(int,input().split())

def bfs(start,end):
    q=deque()
    cnt=0
    q.append((start,cnt))
    founded=False
    
    while q:
        cn,cnt=q.popleft()
        cnt+=1
        #print(f'cn:{cn}, cnt:{cnt}')
        n1=cn*2
        n2=cn*10+1
        
        if n1==end or n2==end:
            print(cnt+1)
            founded=True
            return
        if n1<=end:
            q.append((n1,cnt))
        if n2<=end:
            q.append((n2,cnt))
    
    if not founded:
        print(-1)
        return
    
bfs(a,b)