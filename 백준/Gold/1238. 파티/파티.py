#최단거리,다익스트라,가중치
import sys,heapq
input=sys.stdin.readline
n,m,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
reversed_graph=[[] for _ in range(n+1)]
for _ in range(m):
    start,end,time=map(int,input().split())
    graph[start].append((time,end))
    reversed_graph[end].append((time,start))

#여러 번의 다익스트라를 돌리기 위해 함수화
def dijkstra(start,graph):
    heap=[]
    INF=float('inf')
    dist=[INF]*(n+1)
    dist[start]=0
    
    heapq.heappush(heap,(0,start))
    while heap:
        weight,current_node=heapq.heappop(heap)
        for new_weight,next_node in graph[current_node]:
            cost=weight+new_weight
            if cost<dist[next_node]:
                dist[next_node]=cost
                heapq.heappush(heap,(cost,next_node))
    
    return dist

dist_x_to_all=dijkstra(x,graph)
dist_all_to_x=dijkstra(x,reversed_graph)
dist_sum=[]

for i in range(1,n+1):
    dist_sum.append(dist_x_to_all[i]+dist_all_to_x[i])

print(max(dist_sum))