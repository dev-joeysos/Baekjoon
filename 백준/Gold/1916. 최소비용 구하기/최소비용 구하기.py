import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())
INF = float('inf')
dist = [INF] * (n + 1)
dist[start] = 0

heap = []
heapq.heappush(heap, (0, start))  # (거리, 노드)

while heap:
    cost, now = heapq.heappop(heap)
    
    if dist[now] < cost:
        continue

    for next_node, weight in graph[now]:
        new_cost = cost + weight
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node))

print(dist[end])