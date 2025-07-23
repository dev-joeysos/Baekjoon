# mst, heapq
import sys,heapq
input=sys.stdin.readline

def mst(v,start,graph):
    visited=[False]*(v+1)
    heap=[]
    heapq.heappush(heap,(0,start))
    total=0
    
    while heap:
        cost,current_node=heapq.heappop(heap)
        if visited[current_node]:
            continue
        visited[current_node]=True
        total+=cost
        
        for next_cost,next_node in graph[current_node]:
            if not visited[next_node]:
                heapq.heappush(heap,(next_cost,next_node))
                
    return total
    
def main():
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        a,b,c=map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))
    total_cost=mst(v,1,graph)
    print(total_cost)
    
if __name__=="__main__":
    main()