import sys
input = sys.stdin.readline

n = str(input())
m = n.split('-')

ans = 0

x = sum(map(int, m[0].split('+')))
if n[0] == '-':
    ans -= x
else:
    ans += x

for item in m[1:]:
    x = sum(map(int, item.split('+')))
    ans -= x

print(ans)
