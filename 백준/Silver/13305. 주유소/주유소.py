import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))  # [2 3 1] N개
cost = list(map(int, input().split()))  # [5 2 4 1] N-1개

c = cost[0]
rst = 0
for i in range(n-1):
    if c > cost[i]:
        c = cost[i]
    rst += c*dist[i]
print(rst)
