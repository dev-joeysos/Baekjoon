# 1 일 1 백준
# 230802
N = []
a, b, c = map(int, input().split())
N = [a, b, c]
N.sort()

if N[0]+N[1] <= N[2]:
    print(N[0] + N[1] + (N[0]+N[1]-1))
else:
    print(a+b+c)
