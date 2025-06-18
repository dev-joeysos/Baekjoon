'''
다익스트라=최소거리가 노드 수 만큼 필요
+우선순위 큐
+직전 노드의 기록이 노드 수 만큼 필요(경로 복원할 때)
'''
import sys,heapq
input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    cn,nn,cost=map(int,input().split())
    graph[cn].append((nn,cost)) #다음 노드, 비용

start,end=map(int,input().split())
INF=float('inf')
dist=[INF]*(n+1) #최소거리저장
dist[start]=0
#prev=[0]*(n+1) #직전노드저장
#print(*graph)

heap=[] #우선순위 큐
heapq.heappush(heap,(0,start)) #거리, 노드 번호

while heap:
    #print(*heap)
    cost,current_node=heapq.heappop(heap)
    #print(f'cost={cost}, current_node={current_node}')
    if dist[current_node]<cost:
        continue
    
    for next_node,weight in graph[current_node]:
        new_cost=cost+weight
        # 현재 다음 노드까지 갈 수 있는 최소 비용 > 새로운 노드로 향하는 비용
        if dist[next_node]>new_cost:
            dist[next_node]=new_cost
            # prev[next_node]=current_node 경로 복원시 사용
            heapq.heappush(heap,(new_cost,next_node))

print(dist[end])