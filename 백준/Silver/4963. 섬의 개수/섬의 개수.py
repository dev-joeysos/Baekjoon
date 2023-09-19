from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, -1, -1, 1, 1]

ans = []


def bfs(v):
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        for dir in range(8):
            ni, nj = v[0]+dx[dir], v[1]+dy[dir]
            if 0 <= ni < h and 0 <= nj < w and graph[ni][nj] == 1:
                graph[ni][nj] = 0
                q.append([ni, nj])


while True:
    w, h = map(int, input().split())
    count = 0
    if w == h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs([i, j])
                count += 1
    ans.append(count)

print(*ans, sep='\n')
