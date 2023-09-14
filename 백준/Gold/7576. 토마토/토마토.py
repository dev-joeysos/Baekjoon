from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    global q
    while q:
        ci, cj = q.popleft()
        for dir in range(4):
            ni, nj = ci+dx[dir], cj+dy[dir]
            if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 0:
                q.append([ni, nj])
                graph[ni][nj] = graph[ci][cj] + 1


M, N = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 처음 입력부터 다 익은 상태
found_zero = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            found_zero = True
            break
        if found_zero:
            break

if not found_zero:
    print(0)
    exit()

q = deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i, j])

bfs()

max_depth = 0
for row in graph:
    if 0 in row:
        print(-1)
        exit()
    tmp = max(row)
    max_depth = max(max_depth, tmp)

print(max_depth-1)
