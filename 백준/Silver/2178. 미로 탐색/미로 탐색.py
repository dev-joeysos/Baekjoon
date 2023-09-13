import sys
input = sys.stdin.readline

# dfs/bfs의 depth 활용 문제
def bfs(i, j):
    global v
    q = []
    q.append((i, j))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        ci, cj = q.pop(0)
        v[ci][cj] = True
        for dir in range(4):
            ni, nj = ci+dx[dir], cj+dy[dir]
            if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 1 and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = True
                graph[ni][nj] = graph[ci][cj] + 1  # depth를 저장하면서 경로탐색


N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
v = [[False]*(M) for _ in range(N)]

bfs(0, 0)
print(graph[N-1][M-1])
