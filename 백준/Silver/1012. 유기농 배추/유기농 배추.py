'''
그냥 화가 난다 화가나

'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50 + 10

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(y, x):
    global v
    v[y][x] = True

    for dir in range(4):
        nx, ny = x+dx[dir], y+dy[dir]
        if graph[ny][nx] and not v[ny][nx]:
            dfs(ny, nx)


T = int(input().rstrip())
for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
    graph = [[False]*MAX for _ in range(MAX)]
    v = [[False]*MAX for _ in range(MAX)]

    # 그래프 정보 입력
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        graph[y+1][x+1] = 1

    # 방문하지 않은 지점부터 dfs 돌기
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if graph[i][j] and not v[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
