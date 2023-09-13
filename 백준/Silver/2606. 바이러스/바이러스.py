import sys


def dfs(idx):
    global graph, visited
    visited[idx] = True
    for next in range(1, n+1):
        if graph[idx][next] and not visited[next]:  
            dfs(next)


input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (n+1)
dfs(1)

count = 0
for item in visited:
    if item:  
        count += 1

print(count-1)
