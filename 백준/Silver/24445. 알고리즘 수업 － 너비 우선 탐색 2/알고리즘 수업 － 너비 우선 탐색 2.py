from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, visited, start):
    cnt = 1
    q = deque([])
    q.append(start)
    visited[start] = 1
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append(next_node)
                cnt += 1
                visited[next_node] = cnt


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()
    graph[i].reverse()

bfs(graph, visited, r)

for i in visited[1:]:
    print(i)
