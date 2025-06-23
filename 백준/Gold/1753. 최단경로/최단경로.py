#다익스트라=그래프,우선순위큐,INF
from collections import defaultdict
import sys,heapq
input=sys.stdin.readline
v,e=map(int,input().split())
k=int(input())

graph=defaultdict(list)
for _ in range(e):
    u,to,w=map(int,input().split())
    graph[u].append((to,w)) #다음노드, 가중치
    
heap=[]
heapq.heappush(heap,(0,k)) #가중치, 시작노드

INF=float('inf')
dist=[INF]*(v+1)
dist[k]=0

while heap:
    current_weight,current_node=heapq.heappop(heap)
    #이미 방문한 적이 있는 노드이고, 비용이 더 작은 경우 스킵
    if current_weight>dist[current_node]:
        continue
    
    for neighbor,weight in graph[current_node]:
        cost=current_weight+weight
        #현재 이웃노드로 갈 수 있는 비용보다 짧으면 갱신 가능
        if dist[neighbor]>cost:
            dist[neighbor]=cost
            heapq.heappush(heap,(cost,neighbor))
    
for d in dist[1:]:
    print(d if d!=INF else 'INF')