# n번의 dijkstra
import sys,heapq
input=sys.stdin.readline

def dijkstra(start,n,graph):
    INF=float("inf")
    distance=[INF]*n
    distance[start]=0
    
    heap=[]
    heapq.heappush(heap,(0,start))
    
    while heap:
        weight,current_node=heapq.heappop(heap)
        for new_weight,next_node in graph[current_node]:
            cost=weight+new_weight
            if cost<distance[next_node]:
                distance[next_node]=cost
                heapq.heappush(heap,(cost,next_node))
    
    return distance

def find_max_items_cnt(distance,m,nodes):
    total=0
    for i in range(len(distance)):
        if distance[i]<=m:
           total+=nodes[i]
    return total 

def main():
    n,m,r=map(int,input().split())
    nodes=list(map(int,input().split()))
    graph=[[] for _ in range(n+1)]
    max_val=-1

    for _ in range(r):
        start,end,weight=map(int,input().split())
        start-=1
        end-=1
        graph[start].append((weight,end))
        graph[end].append((weight,start))
    
    for i in range(n):
        distance=dijkstra(i,n,graph)
        max_val=max(max_val,find_max_items_cnt(distance,m,nodes))
    
    print(max_val)
        
if __name__=="__main__":
    main()