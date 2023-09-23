import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
s = [0]
rst = 0
for i in range(n):
    rst += arr[i]
    s.append(rst)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    r = s[b] - s[a-1]
    print(r)