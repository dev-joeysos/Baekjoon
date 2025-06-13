#각 노드의 부모를 구하시오
from collections import defaultdict,deque
import sys
input=sys.stdin.readline
n=int(input())
dict=defaultdict(list)
for _ in range(n-1):
    n1,n2=map(int,input().split())
    dict[n1].append(n2)
    dict[n2].append(n1)

def bfs(start,n,dict):
    q=deque()
    parents=[-1]*(n+1)
    
    q.append(start)
    parents[start]=0
    
    while q:
        current_node=q.popleft()
        
        for next_node in dict[current_node]:#연결된 다음 노드에 대해
            if parents[next_node]==-1:#아직 부모노드가 없다면
                q.append(next_node)
                parents[next_node]=current_node #연결된 노드의 부모 노드는 현재 노드

    for i in range(2,n+1):
        print(parents[i])
    
bfs(1,n,dict)
