'''
보물섬 문제
'''
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
ans = 0


def bfs(i, j):
    q = deque([])
    q.append([i, j, 0])  # 찾은 섬부터 시작
    visited = [[False]*M for _ in range(N)]
    max_depth = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while q:
        ci, cj, depth = q.popleft()
        visited[ci][cj] = True
        max_depth = max(max_depth, depth)
        for dir in range(4):
            ni, nj = ci+dx[dir], cj+dy[dir]
            # 이동이 되면
            if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 'L' and not visited[ni][nj]:
                q.append([ni, nj, depth+1])
                visited[ni][nj] = True
    return max_depth


for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            if 0 <= i-1 and i+1 < N:
                if graph[i-1][j] == 'L' and graph[i+1][j] == 'L':
                    continue
            if 0 < j-1 and j+1 < M:
                if graph[i][j-1] == 'L' and graph[i][j-1] == 'L':
                    continue
            ans = max(ans, bfs(i, j))

print(ans)
