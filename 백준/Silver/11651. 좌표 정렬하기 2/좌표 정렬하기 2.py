N = int(input())
result = []
for _ in range(N):
    x, y = map(int, input().split()) 
    result.append([x, y])

result.sort(key=lambda point: (point[1], point[0]))

for point in result:
    print(point[0], point[1])
