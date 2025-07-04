import sys,heapq
input=sys.stdin.readline

def dijkstra(start,n,graph):
    heap=[]
    heapq.heappush(heap,(0,start)) #(가중치,시작노드)
    INF=float('inf')
    distance=[INF]*(n+1)
    distance[start]=0
    
    while heap:
        current_weight,current_node=heapq.heappop(heap)
        for next_weight,next_node in graph[current_node]:    
            accumulated_weight=current_weight+next_weight
            if accumulated_weight<distance[next_node]:
                distance[next_node]=accumulated_weight
                heapq.heappush(heap,(accumulated_weight,next_node))
    
    return distance

n,e=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(e):
    start,end,weight=map(int,input().split())
    graph[start].append((weight,end))
    graph[end].append((weight,start))

v1,v2=map(int,input().split())

distance_from_start=dijkstra(1,n,graph)
distance_from_v1=dijkstra(v1,n,graph)
distance_from_v2=dijkstra(v2,n,graph)

#1->v1->v2->n
shortest_path1=distance_from_start[v1]+distance_from_v1[v2]+distance_from_v2[n]
#1->v2->v1->n
shortest_path2=distance_from_start[v2]+distance_from_v2[v1]+distance_from_v1[n]
shorest_path=min(shortest_path1,shortest_path2)
print(shorest_path if shorest_path<float('inf') else -1)