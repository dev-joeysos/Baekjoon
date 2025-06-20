#dijkstra
import sys,heapq
input=sys.stdin.readline
n,k=map(int,input().split())
heap=[]
heapq.heappush(heap,(0,n))

INF=float('inf')
MAX=100001
dist=[INF]*MAX
dist[n]=0

while heap:
    total,current_node=heapq.heappop(heap)
    if dist[current_node]<total:
        continue
    #걷기
    for next_node,cost in [(current_node-1,1),(current_node+1,1)]:
        if 0<=next_node<MAX and dist[next_node]>total+cost:
            dist[next_node]=total+cost
            heapq.heappush(heap,(dist[next_node],next_node))
    #순간이동
    next_node=current_node*2
    if next_node<MAX and dist[next_node]>total:
        dist[next_node]=total
        heapq.heappush(heap,(total,next_node))
    
print(dist[k])