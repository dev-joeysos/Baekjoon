import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for _ in range(n):
    x = int(input())
    lst.append(x)

lst.reverse()
ans = 0
for i in range(n):
    if k == 0:
        break
    if k >= lst[i]:
        a = k // lst[i]  # 몫
        k = k % lst[i]  # 나머지로 갱신
        ans += a
print(ans)
