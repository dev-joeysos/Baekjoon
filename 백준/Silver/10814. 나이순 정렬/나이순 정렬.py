import sys
N = int(input())
result = []
for _ in range(N):
    x, y = sys.stdin.readline().split()
    x = int(x)
    result.append([x, y])

result.sort(key=lambda x: (x[0]))

for val in result:
    print(val[0], val[1])
