from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, i, j, visited, rain):
    q = deque([])
    q.append([i, j])
    visited[i][j] = True
    while q:
        ci, cj = q.popleft()
        for dir in range(4):
            ni, nj = ci+dx[dir], cj+dy[dir]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and graph[ni][nj] > rain:
                q.append([ni, nj])
                visited[ni][nj] = True


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_rain = 0
min_rain = 101
for item in graph:
    for i in item:
        max_rain = max(max_rain, i)
        min_rain = min(min_rain, i)

ans = []
for rain in range(min_rain-1, max_rain+1):  # 0~9, min_rain - 1 : 아무 지역도 안 잠김
    count = 0
    visited = [[False]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > rain:
                bfs(graph, i, j, visited, rain)
                count += 1
    ans.append(count)
print(max(ans))
# rain이 내리면
# graph 원소를 지워야 함.
# bfs 탐색에서 rain보다 큰 값만 탐색하면 되지 않나?
