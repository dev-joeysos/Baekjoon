#bfs, 구현
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for y in range(n):
    for x in range(n):
        if board[y][x] == 9:
            sy, sx = y, x
            board[y][x] = 0

size = 2
eat = 0
time = 0

def bfs(y, x, size):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((y, x, 0))
    visited[y][x] = True
    fishes = []
    while q:
        cy, cx, dist = q.popleft()
        for dy, dx in [(-1,0), (0,-1), (0,1), (1,0)]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if board[ny][nx] <= size:
                    visited[ny][nx] = True
                    if 0 < board[ny][nx] < size:
                        fishes.append((dist+1, ny, nx))
                    q.append((ny, nx, dist+1))
    return sorted(fishes)

while True:
    fish_list = bfs(sy, sx, size)
    if not fish_list:
        break
    dist, ny, nx = fish_list[0]
    sy, sx = ny, nx
    board[sy][sx] = 0
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    time += dist

print(time)