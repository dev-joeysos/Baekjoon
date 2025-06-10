from collections import deque
import sys
input=sys.stdin.readline

def bfs(start,distance,goal,ladder,snake):
    q=deque()
    dices=[1,2,3,4,5,6]
    q.append(start)
    distance[start]=1 #시작좌표
    
    while q:
        cp=q.popleft()
        for num in dices:
            np=cp+num
            if np>100:
                continue
            #사다리나 뱀인 경우
            if np in ladder:
                np=ladder[np]
            elif np in snake:
                np=snake[np]
            #방문하지 않았다면
            if distance[np]==0:
                distance[np]=distance[cp]+1
                q.append(np)
                if np==goal:
                    print(distance[np]-1)
                    return
                

#input
n,m=map(int,input().split())
ladder={}
snake={}
for _ in range(n):
    x,y=map(int,input().split())
    ladder[x]=y
    
for _ in range(m):
    u,v=map(int,input().split())
    snake[u]=v

goal=100
distance=[0 for _ in range(101)]

bfs(1,distance,goal,ladder,snake)