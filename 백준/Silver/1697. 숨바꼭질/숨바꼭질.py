import sys
from collections import deque
input = sys.stdin.readline


def bfs(s, e):
    global visited
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        cn = q.popleft()
        if cn == e:
            return visited[cn]-1
        for n in (cn-1, cn+1, cn*2):
            if 0 <= n <= 200000 and visited[n] == 0:
                q.append(n)
                visited[n] = visited[cn] + 1


N, K = map(int, input().split())
visited = [0]*200001
print(bfs(N, K))
