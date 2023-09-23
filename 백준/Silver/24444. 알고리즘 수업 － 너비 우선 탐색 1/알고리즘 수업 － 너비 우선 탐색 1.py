from collections import deque
import sys
input = sys.stdin.readline


def bfs(v, e, r):
    cnt = 1
    q = deque()
    v[r] = True
    q.append(r)
    ans[r] = cnt
    while q:
        cur = q.popleft()
        for i in sorted(e[cur]):
            if not v[i] and 0 < i:
                cnt += 1
                v[i] = True
                q.append(i)
                ans[i] = cnt


n, m, r = map(int, input().split())
e = [[0] for _ in range(n+1)]

v = [False]*(n+1)
ans = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    e[x].append(y)
    e[y].append(x)

bfs(v, e, r)
print(*ans[1:], sep='\n')