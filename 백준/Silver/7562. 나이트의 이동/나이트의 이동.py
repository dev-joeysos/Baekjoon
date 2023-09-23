from collections import deque
import math
import sys
input = sys.stdin.readline

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]


def bfs(x, y, fx, fy):
    cnt = 0
    q = deque([])
    q.append([x, y, 0])
    v[x][y] = True
    while q:
        cx, cy, steps = q.popleft()
        if cx == fx and cy == fy:
            print(steps)
            return
        for dir in range(8):
            nx, ny = cx+dx[dir], cy+dy[dir]
            if 0 <= nx < l and 0 <= ny < l and not v[nx][ny]:
                v[nx][ny] = True
                q.append([nx, ny, steps + 1])


n = int(input())
for _ in range(n):
    l = int(input())
    ix, iy = map(int, input().split())
    fx, fy = map(int, input().split())

    v = [[False] * (l) for _ in range(l)]

    if ix == fx and iy == fy:
        print(0)
    else:
        bfs(ix, iy, fx, fy)
