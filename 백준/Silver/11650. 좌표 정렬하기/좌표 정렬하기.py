# 좌표 정렬
# 튜플로 정렬하기?
N = int(input())
result = []
for _ in range(N):
    x, y = map(int, input().split())
    result.append([x, y])

result.sort()
for point in result:
    print(' '.join(map(str, point)))
