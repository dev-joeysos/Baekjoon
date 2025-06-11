'''
DSLR
'''
from collections import deque
import sys
input=sys.stdin.readline

def bfs(a,b):
    q=deque()
    val=10000
    visited=[False]*val
    route=['']*val
    dir=['D','S','L','R']
    q.append(a)
    visited[a]=True

    while q:
        cp=q.popleft()
        cr=route[cp] #현재 좌표까지의 경로
        for cmd in dir:
            np=0
            nr=''
            if cmd==dir[0]: #D
                np=2*cp%10000
                nr=cr+dir[0]
            elif cmd==dir[1]: #S
                np=cp-1 if cp!=0 else 9999
                nr=cr+dir[1]
            elif cmd==dir[2]: #L
                head=cp//1000
                body=cp%1000
                np=body*10+head
                nr=cr+dir[2]
            else: #R
                head=cp//10
                body=cp%10
                np=body*1000+head
                nr=cr+dir[3]
            if not visited[np]:
                q.append(np)
                visited[np]=True
                route[np]=nr
                if np==b:
                    return route[np]
    
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(bfs(a,b))