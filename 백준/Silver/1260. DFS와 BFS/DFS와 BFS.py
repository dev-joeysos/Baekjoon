'''
DFS/BFS
'''
import sys


def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')

    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:  # 방문할 수 있어
            dfs(next)  # 재귀로 한거야


def bfs():
    global q, visited
    while q:  # 큐가 남아 있을 때까지
        cur = q.pop(0)
        visited[cur] = True
        print(cur, end=' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)


input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

# 간선정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs(V)
print()

visited = [False] * (N+1)
q = [V]
bfs()
