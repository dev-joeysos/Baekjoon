import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(start):
    global count
    visited[start] = True
    ans[start] = count
    graph[start].sort(reverse=True)
    for item in graph[start]:
        if not visited[item]:
            count += 1
            dfs(item)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False]*(n)
ans = [0]*(n)
count = 1
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

dfs(r-1)
print(*ans, sep='\n')
