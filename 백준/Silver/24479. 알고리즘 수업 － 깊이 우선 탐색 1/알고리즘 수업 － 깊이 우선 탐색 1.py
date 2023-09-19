import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node):
    visited[node] = True
    path.append(node)
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
    return


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
path = []
result = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, len(graph)):
    graph[i].sort()
dfs(r)

for idx, node in enumerate(path, start=1):
    result[node] = idx

print(*result[1:], sep="\n")
