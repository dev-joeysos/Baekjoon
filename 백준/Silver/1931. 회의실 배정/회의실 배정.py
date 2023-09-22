import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append([x, y])

lst.sort(key=lambda x: x[0])
lst.sort(key=lambda x: x[1])

cnt = 1
end = lst[0][1]
for i in range(1, n):
    if lst[i][0] >= end:
        cnt += 1
        end = lst[i][1]
print(cnt)
