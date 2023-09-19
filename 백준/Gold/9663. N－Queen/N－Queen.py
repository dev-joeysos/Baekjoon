import sys
input = sys.stdin.readline

n = int(input())
v1, v2, v3 = [[0]*(2*n) for _ in range(3)]
ans = 0


def dfs(row):
    global ans
    if row == n:
        ans += 1
        return
    for j in range(n):
        if v1[j] == v2[row+j] == v3[row-j] == 0:
            v1[j] = v2[row+j] = v3[row-j] = 1
            dfs(row+1)
            v1[j] = v2[row+j] = v3[row-j] = 0


dfs(0)
print(ans)