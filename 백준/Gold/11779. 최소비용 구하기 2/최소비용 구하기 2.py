# dijkstra
import sys,heapq
input=sys.stdin.readline

def dijkstra(start,graph,n):
    INF=float('inf')
    distance=[INF]*(n+1)
    distance[start]=0
    heap=[]
    heapq.heappush(heap,(0,start))
    prev=[0]*(n+1)
    
    while heap:
        weight,current=heapq.heappop(heap)
        
        if distance[current]<weight: # 이미 더 짧은 경로라면 생략
            continue
        
        for new_weight,next in graph[current]:
            cost=weight+new_weight
            if cost<distance[next]:
                distance[next]=cost
                prev[next]=current
                heapq.heappush(heap,(cost,next))
   
    return distance, prev
 
def find_path(prev,s,e):
    path=[]
    node=e
    while node!=0:
        path.append(node)
        node=prev[node]
    path.reverse() 
    return path
 
def main():
    n=int(input())
    m=int(input())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        start,end,weight=map(int,input().split())
        graph[start].append((weight,end))
    s,e=map(int,input().split())
    
    distance,prev=dijkstra(s,graph,n)
    path=find_path(prev,s,e)
    
    print(distance[e])
    print(len(path))
    print(' '.join(map(str,path)))

if __name__=="__main__":
    main()