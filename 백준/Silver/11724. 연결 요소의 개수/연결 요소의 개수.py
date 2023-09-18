from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, graph, visited):
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        v = q.popleft()
        for node in graph[v]:
            # 검사조건 추가
            if not visited[node]:
                q.append(node)
                visited[node] = True


N, M = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
count = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    if not visited[i]:
        bfs(i, graph, visited)
        count += 1
print(count)
