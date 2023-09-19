import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 약수 찾기
s = min(n, m)
a1 = []
a2 = []
for i in range(1, s+1):
    tmp1 = n / i
    tmp2 = m / i

    if int(tmp1) == tmp1:
        a1.append(i)
        a1.append(int(tmp1))
    if int(tmp2) == tmp2:
        a2.append(i)
        a2.append(int(tmp2))

ans = []
for item in a1:
    if item in a2:
        ans.append(item)

S = max(ans)
print(S)

rst = (n*m)//S
print(rst)
