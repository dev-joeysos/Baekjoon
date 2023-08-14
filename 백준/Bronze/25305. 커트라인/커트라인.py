# 커트라인
# 점수가 높은 k명이 수상
# 상을 받는 커트라인 점수

N, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr.reverse()
print(arr[k-1])
