import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    global v
    q = []
    q.append((i, j))
    cnt = 0
    while q:
        ci, cj = q.pop(0)
        cnt += 1
        v[ci][cj] = True
        for dir in range(4):
            ni, nj = ci+dx[dir], cj+dy[dir]
            if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] == 1 and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = True
    return cnt


N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
v = [[False]*(N) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not v[i][j]:
            rst = bfs(i, j)
            ans.append(rst)
ans.sort()
print(len(ans), *ans, sep='\n')
